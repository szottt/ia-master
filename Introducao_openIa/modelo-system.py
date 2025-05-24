from openai import OpenAI
#from Configs.api import api_key
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')


client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
      {
        'role': 'system',
        'content': 'Voce sera um tradutor de textos de portugues para ingles.'
      },
      {
        'role':'user',
        'content': 'O Livro esta na mesa.'
      }  
    ],
    #max_tokens=200,
    #temperature=0.8
)

print(response.choices[0].message.content)
