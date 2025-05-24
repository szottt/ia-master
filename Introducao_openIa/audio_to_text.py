from openai import OpenAI
from Configs.path import caminho_audio
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')


client = OpenAI(api_key=api_key)

audio_file = open(f'{caminho_audio}/meu_audio_nova2.mp3', 'rb')

texto = client.audio.transcriptions.create(
    model='whisper-1',
    file=audio_file
)

print(texto.text)