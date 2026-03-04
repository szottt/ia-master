import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
os.getenv('OPENAI_API_KEY')

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

# if question:
#     with chat_container:
#         st.chat_message('user').write(question)
#         st.chat_message('assistant').write("Estou processando sua pergunta...")