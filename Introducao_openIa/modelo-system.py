from openai import OpenAI
from api import api_key

client = OpenAI(
    api_key=f"{api_key}"
)

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
