from openai import OpenAI
#from api import *
from Configs.path import caminho_audio
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')


client = OpenAI(api_key=api_key)

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