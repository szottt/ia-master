from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()
os.getenv('OPENAI_API_KEY')

model = ChatOpenAI(
    model='gpt-3.5-turbo',
)

prompt_tamplate = PromptTemplate.from_template(
    'Me fale sobre o jogo {jogo}'
)

# runnable_sequence = prompt_tamplate | model | StrOutputParser()

# response = runnable_sequence.invoke({'jogo': 'Counter Strike'})

# print(response)

chain = (
    PromptTemplate.from_template(
    'Me fale sobre o jogo {jogo}'
    )
    | model
    | StrOutputParser()
)

response = chain.invoke({'jogo': 'Counter Strike'})

print(response)