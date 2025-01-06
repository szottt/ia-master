from langchain_openai import OpenAI, ChatOpenAI
from langchain.prompts import PromptTemplate
from Configs.api import api_key
import os

os.environ['OPENAI_API_KEY'] = f'{api_key}'

model = ChatOpenAI(
    model='gpt-3.5-turbo',
)

template = '''
Traduza o texto do Idioma {idioma1} para o {idioma2}
{texto}
'''

prompt_template = PromptTemplate.from_template(
    template = template
)

prompt = prompt_template.format(
    idioma1 = 'português',
    idioma2 = 'Polones',
    texto = 'Boa Dia!',
)

response = model.invoke(prompt)

print(response.content)