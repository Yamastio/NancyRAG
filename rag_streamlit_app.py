import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from vector import md_rag
import os

# --- Inisialisasi model ---
ollama_url = os.environ.get("OLLAMA_API_BASE", "http://localhost:11434")
model = OllamaLLM(model="llama3.2:3b", base_url=ollama_url)

# --- Template prompt ---
template = """
You are an expert answering technical questions using the following documents:
{documents}

Question: {question}
Answer in detail, structured, and in Indonesian.
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# --- Retriever untuk Markdown files ---
md_files = "./markdown_files"
retriever = md_rag(
    source_directory=md_files,
    db_path="chroma_md_db",
    collection_name="tech_files"
)

# --- Streamlit UI ---
st.set_page_config(page_title="NancyRAG", page_icon="🤖")
st.title("NancyRAG")

# Menyimpan history chat
if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.chat_input("Ask something...")
if user_input:
    docs = retriever.invoke(user_input)
    answer = chain.invoke({"documents": docs, "question": user_input})
    st.session_state.history.append({"user": user_input, "bot": answer})

# Render semua chat
for chat in st.session_state.history:
    with st.chat_message("user"):
        st.markdown(chat["user"])
    with st.chat_message("assistant"):
        st.markdown(chat["bot"])
