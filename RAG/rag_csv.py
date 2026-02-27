import os
from dotenv import load_dotenv
from langchain import hub
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import CSVLoader
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()
os.getenv('OPENAI_API_KEY')

model = ChatOpenAI(model='gpt-3.5-turbo')
pdf_path = '/home/vkn/projetos/eng/python/ia-master/RAG/files/carros.csv'
loader = CSVLoader(pdf_path)

docs = loader.load()

text_spliter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

chunks = text_spliter.split_documents(documents=docs)

persist_directory = 'db'

embeddings = OpenAIEmbeddings()

vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    collection_name='carros',
    persist_directory=persist_directory
)

