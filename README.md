# Curso de IA com Python

Este projeto é um curso de Inteligência Artificial (IA) utilizando Python. O primeiro módulo, chamado "Introducao_openIa", contém cinco scripts que demonstram diferentes funcionalidades da API OpenAI.

## Estrutura do Projeto

ia-master/ │ ├── Introducao_openIa/ │ ├── audio_gen.py │ ├── audio_to_text.py │ ├── imagem_gen.py │ ├── modelo-system.py │ └── resposta-stream.py └── api.py

## Scripts

### 1. `audio_gen.py`

Este script gera um arquivo de áudio a partir de um texto utilizando a API de síntese de voz da OpenAI.

```python
from openai import OpenAI
from api import *
import os

client = OpenAI(api_key=f"{api_key}")
response = client.audio.speech.create(
    model='tts-1',
    voice='nova',
    input='Estou fazendo meu primeiro curso de inteligencia artificial',
)

# Define the directory and file path
directory = f'{caminho_audio}'
file_path = os.path.join(directory, 'meu_audio_nova2.mp3')

# Now you can safely write the file
response.write_to_file(file_path)
```

### 2. `audio_to_text.py`

Este script converte um arquivo de áudio em texto utilizando a API de transcrição da OpenAI.

```python
from openai import OpenAI
from api import *
import os

client = OpenAI(api_key=f"{api_key}")
audio_file = open(f'{caminho_audio}/meu_audio_nova2.mp3', 'rb')
texto = client.audio.transcriptions.create(
    model='whisper-1',
    file=audio_file
)
print(texto.text)

```



### 3. `imagem_gen.py`

Este script gera uma imagem a partir de um prompt utilizando a API DALL-E da OpenAI.
```python
from openai import OpenAI
from api import api_key

client = OpenAI(api_key=f"{api_key}")
response = client.images.generate(
    model='dall-e-3',
    prompt="Faça uma imagem de um streamer porem que fica no lugar dele é a sua cadeira",
    size="1024x1024",
    quality="standard",
    n=1,
)
image_url = response.data[0].url
print(image_url)

```

### 4. `modelo_system.py`

Este script utiliza a API GPT para traduzir textos do português para o inglês.
```python
from openai import OpenAI
from api import api_key

client = OpenAI(api_key=f"{api_key}")
response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {
            'role': 'system',
            'content': 'Voce sera um tradutor de textos de portugues para ingles.'
        },
        {
            'role': 'user',
            'content': 'O Livro esta na mesa.'
        }   
    ],
)
print(response.choices[0].message.content)

```

### 5. `resposta_stream.py`

Este script utiliza a API GPT para gerar respostas em tempo real a partir de um prompt.

```python
from openai import OpenAI
from api import api_key

client = OpenAI(api_key=f"{api_key}")
stream = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {'role':'user', 'content': 'Me fale sobre o Fiat Elba 1988'}   
    ],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end='')

```

## Inclusao do Modulo 2