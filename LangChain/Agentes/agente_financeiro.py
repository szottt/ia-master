import os
from dotenv import load_dotenv
from langchain import hub
from langchain.agents import Tool, create_react_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_experimental.utilities.python import PythonREPL
from langchain_community.utilities import SerpAPIWrapper

load_dotenv()
os.getenv('OPENAI_API_KEY')
serpapi_api_key = os.getenv('SERPAPI_API_KEY')  # Adicione sua chave SerpAPI no .env

model = ChatOpenAI(model='gpt-3.5-turbo')

prompt = '''
Como assistente financeiro pessoal, responda SEMPRE pesquisando as melhores dicas na internet usando a ferramenta Google Search ANTES de responder.
Responda todas as perguntas em Portugues Brasileiro.
Pergunta: {query}
'''

prompt_template = PromptTemplate.from_template(prompt)

python_repl = PythonREPL()
python_repl_tool = Tool(
    name='Python REPL',
    description='Um shell python. Use isso para executar codigos python. Execute codigos validos apenas'
    'Se voce precisar obter o retorno do codigo use a função "print(...)".'
    'Use para realizar calculos financeiros necessarios para responder as perguntas do usuario',
    func=python_repl.run
)

search = SerpAPIWrapper(serpapi_api_key=serpapi_api_key)
google_tool = Tool(
    name='Google Search',
    description='Util para encontrar informações e dicas de economia e opções de investimento.'
    'Voce sempre deve pesquisar na internet as melhores dicas usando esta ferramenta'
    'responda diretamente. Sua resposta deve informar que ha elementos de pesquisa na internet.',
    func=search.run
)

tools = [python_repl_tool, google_tool]  # Só Google Search e Python REPL
react_instructions = hub.pull('hwchase17/react')

agent = create_react_agent(
    llm=model,
    tools=tools,
    prompt=react_instructions
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)

question = '''
Minha renda é de R$10000 por mes, o total de minhas despesas é de R$8500 mais 1000 de aluguel
Quais dicas de investimento voce me da?
'''

output = agent_executor.invoke(
    {'input': prompt_template.format(query=question)}
)

print(output.get('output'))