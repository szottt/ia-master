import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_experimental.utilities.python import PythonREPL
from langchain.agents import Tool
from langchain_experimental.agents.agent_toolkits import create_python_agent
from langchain.prompts import PromptTemplate

load_dotenv()
os.getenv('OPENAI_API_KEY')

model = ChatOpenAI(model='gpt-3.5-turbo')
python_repl = PythonREPL()
python_repl_tool = Tool(
    name='Python REPL',
    description='Um Shell python. Use isso para executar codigos python. Execute isso apenas para codigo python'
                'Se voce precisar obter o retorno do codigo use a função "print(...)".',
    func=python_repl.run
)

agente_executor = create_python_agent(
    llm=model,
    tool=python_repl_tool,
    verbose=True
)

prompt_template = PromptTemplate(
    input_variables=['query'],
    template='Resolva o calculo: {query}'
)
#query = '20 x 50'
query = r'Quanto é 20% de 3000'
prompt = prompt_template.format(query=query)
response = agente_executor.invoke(prompt)
print(response.get('output'))