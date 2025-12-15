from langchain_experimental.utilities import PythonREPL

python_rpl = PythonREPL()
result = python_rpl.run('print(5 * 5)')
print(result)
