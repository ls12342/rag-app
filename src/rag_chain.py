# rag_chain.py

from langchain_community.document_loaders import WebBaseLoader
from langchain.document_loaders.pdf import PyPDFDirectoryLoader
from src.data_loader import process_documents
import ollama

# Main function to process documents from a URL or a PDF directory and generate a response to a question
def rag_chain(url, pdf_directory_path, question):
    formatted_context = ""
    if pdf_directory_path is not None and pdf_directory_path.strip():
        loader = PyPDFDirectoryLoader(pdf_directory_path)
        formatted_context += process_documents(loader, question)
        
    if url is not None and url.strip():
        loader = WebBaseLoader([url])
        formatted_context += process_documents(loader, question)
        
    formatted_context = ' '.join(formatted_context.split())
    formatted_prompt = f"Question: {question}\n\nContext: {formatted_context}"
    response = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': formatted_prompt}])
    return response['message']['content']