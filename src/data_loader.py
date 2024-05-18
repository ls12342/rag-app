# document_processing.py

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

# Function to load documents and split them into chunks
def load_and_retrieve_docs(loader):
    try:
        docs = loader.load()
    except Exception as e:
        print(f"Error loading documents: {e}")
        return []
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return text_splitter.split_documents(docs)

# Function to create a Chroma vector store from the document chunks
def add_to_chroma(splits):
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectorestore = Chroma.from_documents(documents=splits, embedding=embeddings)
    return vectorestore

# Function to retrieve documents related to a question from the vector store
def retrieve_docs(vectorestore, question):
    retriever = vectorestore.as_retriever()
    return retriever.invoke(question)

# Function to combine the retrieved documents into a single string
def combine_docs(docs):
    return "\n\n".join(doc.page_content.strip()  for doc in docs)

# Function to process documents: load, split, add to vector store, retrieve and combine
def process_documents(source, question):
    docs = load_and_retrieve_docs(source)
    vectorstore = add_to_chroma(docs)
    retrieved_docs = retrieve_docs(vectorstore, question)
    return combine_docs(retrieved_docs)