from langchain_openai import OpenAI, ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv()
os.getenv('OPENAI_API_KEY')

model = ChatOpenAI(
    model='gpt-3.5-turbo',
)

chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content='Você deve responder baseado em dados geograficos de Regioes do Brasil'),
        HumanMessagePromptTemplate.from_template('Por favor me fale sobre a Região {regiao}.'),
        AIMessage(content='Claro, vou começar coletando informações sobre a regiao e analisando os dados disponiveis.'),
        HumanMessage(content='Certifique-se de incluir dados demograficos.'),
        AIMessage(content='Entendido, aqui estao os dados.'),
    ]
)

prompt = chat_template.format_messages(regiao='Sul')

response = model.invoke(prompt)

print(response.content)