import os
from dotenv import load_dotenv
from langchain import hub
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()
os.getenv('OPENAI_API_KEY')

model = ChatOpenAI(model='gpt-3.5-turbo')

pdf_path = '/home/vkn/projetos/eng/python/ia-master/RAG/files/laptop_manual.pdf'
loader = PyPDFLoader(pdf_path)

docs = loader.load()

text_spliter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

chunks = text_spliter.split_documents(documents=docs)

embeddings = OpenAIEmbeddings()

vector_store = Chroma.from_documents(documents=chunks,
                                     embedding=embeddings,
                                     collection_name='laptop_manual',
                                     )
retriver = vector_store.as_retriever()

prompt = hub.pull('rlm/rag-prompt')

rag_chain = (
    {
    'context': retriver,
    'question': RunnablePassthrough()
    }
    | prompt
    | model
    | StrOutputParser()
)

try:
    while True:
        question = input('Qual a sua duvida: ')
        response = rag_chain.invoke(question)
        print(response)
except KeyboardInterrupt:
    exit()
