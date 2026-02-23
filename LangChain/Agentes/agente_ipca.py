import os
from dotenv import load_dotenv
from langchain import hub
from langchain.agents import Tool, create_react_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_community.utilities.sql_database import SQLDatabase 
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit

load_dotenv()
os.getenv('OPENAI_API_KEY')
serpapi_api_key = os.getenv('SERPAPI_API_KEY')  # Adicione sua chave SerpAPI no .env

model = ChatOpenAI(model='gpt-4-turbo')

db_path = '/home/vkn/projetos/eng/python/ia-master/ipca.db'

db = SQLDatabase.from_uri(f"sqlite:///{db_path}")

toolkit = SQLDatabaseToolkit(
    db=db,
    llm=model,
)

system_message = hub.pull('hwchase17/react')

agent = create_react_agent(
    llm=model,
    tools=toolkit.get_tools(),
    prompt=system_message
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=toolkit.get_tools(),
    verbose=True
)

prompt = '''
    Use as ferramentas necessarias para responder perguntas relacionadas ao historico de IPCA ao longo dos anos.
    Responda todas as perguntas em Portugues Brasileiro.
    Pergunta: {q}
'''

prompt_template = PromptTemplate.from_template(prompt)  

question = '''
Baseado nos dados historicos de IPCA desde 2004, usando matematica estatistica, faça uma previsao dos valores de IPCA de cada mes até o final de 2024.
'''

output = agent_executor.invoke(
    {
        'input': prompt_template.format(q=question)
    }
)

print(output.get('output'))

