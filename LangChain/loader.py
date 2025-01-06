import sys
import os

# Add the parent directory to PYTHONPATH
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from langchain_openai import OpenAI, ChatOpenAI
from Configs.api import api_key  # Import directly from api.py
from Configs.path import path_files  # Import directly from path.py
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader, PyPDFLoader, CSVLoader


os.environ['OPENAI_API_KEY'] = f'{api_key}'

model = ChatOpenAI(
    model='gpt-3.5-turbo',
)

#loader = TextLoader(f'{path_files}/base_conhecimento.txt')
#loader = PyPDFLoader(f'{path_files}/base_conhecimento.pdf')
loader = CSVLoader(f'{path_files}/base_conhecimento.csv')
documents = loader.load()

prompt_base_de_conhecimento = PromptTemplate(
    input_variables=['context', 'pergunta'],
    template='''Use o seguinte contexto para responder a pergunta.
    Responda apenas com base nas informações fornecidas.
    Não utilize informações externas ao contexto:
    Contexto: {contexto}
    Pergunta: {pergunta}'''
)

chain = prompt_base_de_conhecimento | model | StrOutputParser()

response = chain.invoke(
    {
        'contexto': '\n'.join(doc.page_content for doc in documents),
        #'pergunta': 'Qual Oleo de motor devo usar? E tambem qual pneu devo comprar?'
        'pergunta': 'Qual Oleo de motor devo usar?'
    }
)

print(response)