from time import process_time_ns
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

from vector import md_rag
import os

ollama_url = os.environ.get("OLLAMA_API_BASE", "http://localhost:11434")
model = OllamaLLM(model="llama3.2:3b", base_url=ollama_url)

template = """
You are an expert answering technical questions using the following documents:
{documents}

Question: {question}
Answer in detail, structured, and in Indonesian.
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

md_files = "./markdown_files"
retriever = md_rag(source_directory=md_files,
                   db_path="chroma_md_db", collection_name="tech_files")
print("Retriever ready.")

while True:
    print("\n----------------------------------------")
    question = input("Ask your questions (q to quit): ")
    print("\n\n")
    if question == "q":
        break

    docs = retriever.invoke(question)
    result = chain.invoke({"documents": docs, "question": question})
    print(f"AI: {result}")
