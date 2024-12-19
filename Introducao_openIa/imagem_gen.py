from openai import OpenAI
from api import api_key

client = OpenAI(
    api_key=f"{api_key}"
)

response = client.images.generate(
    model='dall-e-3',
    prompt="Faça uma imagem de um streamer porem que fica no lugar dele é a sua cadeira",
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = response.data[0].url

print(image_url)
