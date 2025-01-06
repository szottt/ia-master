from langchain_openai import OpenAI
from langchain_community.cache import InMemoryCache, SQLiteCache
from langchain.globals import set_llm_cache
from Configs.api import api_key
import os

os.environ['OPENAI_API_KEY'] = f'{api_key}'

model = OpenAI()

set_llm_cache(
    SQLiteCache(database_path='openia_cache.db')
)

prompt = 'Me diga quem foi Alan Turing?'

response1 = model.invoke(prompt)
print(f'Chamada 1: {response1}')

response2 = model.invoke(prompt)
print(f'Chamada 2: {response2}')