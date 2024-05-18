# main.py

import gradio as gr
from src.rag_chain import rag_chain

iface = gr.Interface(
    fn=rag_chain,
    inputs=["text", "text", "text"],
    outputs="text",
    title="RAG Question Answering",
)
