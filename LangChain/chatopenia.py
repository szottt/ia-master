from langchain_openai import OpenAI, ChatOpenAI
from Configs.api import api_key
import os

os.environ['OPENAI_API_KEY'] = f'{api_key}'

model = ChatOpenAI(
    model='gpt-3.5-turbo',
)

messages=[
      {
        'role': 'system',
        'content': 'Você é um assistente que fornece informações sobre figuras historicas.'
      },
      {
        'role':'user',
        'content': 'Quem foi Alan Turing?'
      }  
    ]


response = model.invoke(messages)

print(response)
print(response.content)