from openai import OpenAI
from Configs.api import api_key
from Configs.path import caminho_audio
import os

client = OpenAI(
    api_key=f"{api_key}"
)

audio_file = open(f'{caminho_audio}/meu_audio_nova2.mp3', 'rb')

texto = client.audio.transcriptions.create(
    model='whisper-1',
    file=audio_file
)

print(texto.text)