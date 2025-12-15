from langchain_community.tools import DuckDuckGoSearchRun

ddf_search = DuckDuckGoSearchRun()
result = ddf_search.run('Quem foi allan turing?')

print(result)
