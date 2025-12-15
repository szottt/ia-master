from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')


client = OpenAI(api_key=api_key)

stream = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
      {'role':'user',
       'content': 'Me fale sobre o Fiat Elba 1988'}  
    ],
    stream=True,
)

#print(response.choices[0].message.content)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end='')