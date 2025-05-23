from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
os.getenv('OPENAI_API_KEY')

model = OpenAI()

response = model.invoke(
    input='Quem foi Alan Turing?',
    temperature=1,
    max_tokens=300, 
)

print(response)