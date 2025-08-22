import gradio as gr
from vector import md_rag  # pipeline RAG kamu
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import os

# Setting model
ollama_url = os.environ.get("OLLAMA_API_BASE", "http://localhost:11434")
model = OllamaLLM(model="llama3.2:3b", base_url=ollama_url)

# Template prompt RAG
template = """
You are an expert answering technical questions using the following documents:
{documents}

Question: {question}
Answer in detail, structured, and in Indonesian.
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Load vector store
md_files = "./markdown_files"
retriever = md_rag(source_directory=md_files,
                   db_path="chroma_md_db", collection_name="tech_files")
print("Retriever ready.")

# Fungsi untuk Gradio


def answer_question(question):
    docs = retriever.invoke(question)
    result = chain.invoke({"documents": docs, "question": question})
    return result


# Buat interface Gradio
iface = gr.Interface(
    fn=answer_question,
    inputs=gr.Textbox(label="Enter Question",
                      placeholder="Ask anything..."),
    outputs=gr.Textbox(label="Answer"),
    title="Nancy RAG",
    description="Ask for indexed Markdown documents."
)

# Jalankan app
iface.launch()
