import os
from dotenv import load_dotenv
from langchain import hub
from langchain.agents import Tool, create_react_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_experimental.utilities.python import PythonREPL
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_experimental.utilities.python import PythonREPL

load_dotenv()
os.getenv('OPENAI_API_KEY')

model = ChatOpenAI(model='gpt-3.5-turbo')

prompt = '''
Como assistente financeiro pessoal, responda SEMPRE pesquisando as melhores dicas na internet usando a ferramenta DuckDuckGo Search ANTES de responder.
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

search = DuckDuckGoSearchRun()
duckduckgo_tool = Tool(
    name='DuckDuckGo Search',
    description='Util para encontrar informações e dicas de economia e opções de investimento.'
    'Voce sempre deve pesquisar na internet as melhores dicas usando esta ferramenta'
    'responda diretamente. Sua resposta deve informar que ha elementos de pesquisa na internet.',
    func=search.run
)

react_instructions = hub.pull('hwchase17/react')

tools = [python_repl_tool, duckduckgo_tool]

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