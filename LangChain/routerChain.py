from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()
os.getenv('OPENAI_API_KEY')

model = ChatOpenAI(
    model='gpt-3.5-turbo',
)

classification_chain = (
    PromptTemplate.from_template(
        '''
        Classifique a pergunta do usuario em um dos seguintes setores:
        
        - Financeiro
        - Suporte Tecnico
        - Outras informações
        
        Pergunta: {pergunta}
        '''
    )
    | model
    | StrOutputParser()
)

financial_chain = (
    PromptTemplate.from_template(
        '''
        Voce é um especialista financeiro.
        Sempre responda as perguntas começando com "Bem vindo ao Setor Financeiro".
        Responda a pergunta do usuario:
        Pergunta: {pergunta}
        '''
    )
    | model
    | StrOutputParser()
)

tech_support_chain = (
    PromptTemplate.from_template(
        '''
        Voce é um especialista em suporte técnico.
        Sempre responda as perguntas começando com "Bem vindo ao Suporte Técnico".
        Responda a pergunta do usuario:
        Pergunta: {pergunta}
        '''
    )
    | model
    | StrOutputParser()
)

other_info_chain = (
    PromptTemplate.from_template(
        '''
        Voce é um assistente de informações gerais.
        Sempre responda as perguntas começando com "Bem vindo ao setor de Central de Informaçoes Gerais".
        Responda a pergunta do usuario:
        Pergunta: {pergunta}
        '''
    )
    | model
    | StrOutputParser()
)

def route(classification):
    classification = classification.lower()
    if 'financeiro' in classification:
        return financial_chain
    elif 'técnico' in classification:
        return tech_support_chain
    else: 
        return other_info_chain

pergunta = input('Qual a sua pergunta? ')

classification = classification_chain.invoke(
    {'pergunta':pergunta}
)

response_chain = route(classification=classification)

response = response_chain.invoke(
    {'pergunta':pergunta}
)

print(response)