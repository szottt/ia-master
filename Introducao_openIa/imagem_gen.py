from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')


client = OpenAI(api_key=api_key)

response = client.images.generate(
    model='dall-e-3',
    prompt="Faça uma imagem de um streamer porem que fica no lugar dele é a sua cadeira",
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = response.data[0].url

print(image_url)
