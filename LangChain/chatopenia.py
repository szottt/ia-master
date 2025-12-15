from langchain_openai import OpenAI, ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
os.getenv('OPENAI_API_KEY')

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