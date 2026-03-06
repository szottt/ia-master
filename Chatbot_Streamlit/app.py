import streamlit as st
import os
import tempfile
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


load_dotenv()
os.getenv('OPENAI_API_KEY')

persist_directory = 'db'

def process_pdf(file):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
        tmp_file.write(file.read())
        tmp_file_path = tmp_file.name
    
    loader = PyPDFLoader(tmp_file_path)
    docs = loader.load()
    
    os.remove(tmp_file_path)
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=400
        )
    chunks = text_splitter.split_documents(documents=docs)
    return chunks

st.set_page_config(
        page_title="Chat GPT com Python", page_icon=""
        )

st.header('🤖 Chat com seus documentos (RAG) 🤖')

with st.sidebar:
    st.header('Upload de arquivos')
    upload_files = st.file_uploader(
        label="Faça upload dos seus arquivos pdf",
        type=['pdf'],
        accept_multiple_files=True,
        )
    
    if upload_files:
        with st.spinner('Processando documentos...'):
            all_chunks = []
            for upload_files in upload_files:
                chunks = process_pdf(file=upload_files)
                all_chunks.extend(chunks)
            print(all_chunks)
            

    model_options = [            
        "gpt-3.5-turbo",
        "gpt-4",
        "gpt-4-turbo",
        "gpt-4o-mini",
        "gpt-4o"
        ]

    selected_model = st.sidebar.selectbox(
            label="Selecione o modelo de LLM", 
            options=model_options
        )

# espaço para futuras mensagens
chat_container = st.container()

# input SEMPRE por último
question = st.text_input('Como posso ajudar?')

if question:
    with chat_container:
        st.chat_message('user').write(question)
        st.chat_message('assistant').write("Estou processando sua pergunta...")