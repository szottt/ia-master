from langchain_openai import OpenAI
from Configs.api import api_key
import os

os.environ['OPENAI_API_KEY'] = f'{api_key}'

model = OpenAI()

response = model.invoke(
    input='Quem foi Alan Turing?',
    temperature=1,
    max_tokens=300, 
)

print(response)