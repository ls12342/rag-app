# RAG Application with Ollama 3

## Overview

This repository contains a Retrieval-Augmented Generation (RAG) application designed to load websites and PDF files and answer any questions posed to the model (LLama 3). The application is built using Python, LangChain, ChromaDB, and Gradio for the user interface. Embeddings are generated using the nomic-embed-text model.

## Features

- **Data Ingestion**: Load and preprocess websites and PDF files.
- **Question Answering**: Utilize Ollama 3 model for generating answers based on ingested data.
- **User Interface**: Interactive UI built with Gradio for seamless user experience.
- **Database Management**: Efficient data storage and retrieval using ChromaDB.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- [Python 3.12](https://www.python.org/downloads/release/python-3120/)
- [Pip](https://pypi.org/project/pip/) (Python package installer)
- [Conda](https://www.anaconda.com/)
- [Ollama](https://ollama.com/)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/rag-ollama3.git
   cd rag-ollama3
   ```

2. Create a virtual environment:

   ```bash
   conda create -n rag
   conda activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Pull LLama3 model:
   ```bash
   ollama pull llama3
   ```
5. Pull nomic-embed-text model:
   ```bash
   ollama pull nomic-embed-text
   ```

### Running the Application

To start the application, run:

```bash
python app.py
```

The Gradio interface will launch, and you can access it via your web browser at http://127.0.0.1:7860.

### Using another model

1. Pull the desired model:
   ```bash
   ollama pull mistral
   ```
2. Update line 55 to:
   ```python
   response = ollama.chat(model='mistral', messages=[{'role': 'user', 'content': formatted_prompt}])
   ```

### Project Structure

```bash
    rag-app/
    ├── app.py             # Main application script
    ├── data/              # Directory for storing pdf files
    ├── requirements.txt   # Python dependencies
    ├── src/               # Source code directory
    │   ├── data_loader.py # Scripts for loading data
    │   ├── ui.py        # Gradio UI
    │   └── rag_chain.py   # Model handling and inference
    └── README.md          # This README file
```

### Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgements

- [LangChain](https://github.com/langchain/langchain)
- [ChromaDB](https://github.com/chromadb/chromadb)
- [Gradio](https://github.com/gradio-app/gradio)
- [Ollama 3](https://www.ollama.com)
- [nomic-embed-text](https://www.nomic.ai/)

### License

This project is licensed under the MIT License. See the LICENSE file for more details.
