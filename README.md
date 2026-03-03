# PDF RAG Application (Streamlit) #

This project is a simple Retrieval-Augmented Generation (RAG) application built using Streamlit.
It allows users to upload a PDF file and ask questions based on the document’s content. The system retrieves relevant sections from the PDF and generates answers using an LLM.

## What This Project Does

- Upload a PDF file
- Extract text from the document
- Split text into smaller chunks
- Generate embeddings
- Store embeddings in a vector store
- Retrieve relevant chunks when a question is asked
- Generate answers based only on the document content
- The goal of this project was to understand how RAG pipelines work in practice.

## Project Structure

### utils/

- `embedder.py` → Generates vector embeddings for text chunks  
- `llm.py` → Handles interaction with the language model  
- `pdf_loader.py` → Extracts and preprocesses text from PDF files  
- `text_split.py` → Splits extracted text into manageable chunks  
- `vector_store.py` → Stores embeddings and performs similarity-based retrieval  

### Root Directory

- `streamlit_app.py` → Main application interface and user interaction logic  
- `.gitignore` → Specifies files ignored by Git  
- `requirements.txt` → Project dependencies

## How to Run

- Clone the repository
- Create a virtual environment
- Install dependencies
- Add your API key (if required)
- Run:
    streamlit run streamlit_app.py

## Why I Built This

I built this project to deeply understand how Retrieval-Augmented Generation (RAG) systems work beyond theory. Instead of just calling an API, I wanted to learn how:
- Text is chunked efficiently for semantic retrieval
- Embeddings represent meaning mathematically
- Vector databases retrieve context using similarity search
- LLMs generate grounded answers instead of hallucinating
  
This project helped me understand the complete pipeline — from raw document ingestion to context-aware answer generation.
It also allowed me to practice modular project design by separating embedding logic, vector storage, LLM interaction, and UI into different components.

## Future Improvements

- Add persistent vector storage
- Improve UI
- Add chat history memory
- Deploy online

## Author
- Simran Prabhakar (AI & Machine Learning Enthusiast)
- GitHub: https://github.com/simranprabhakar

## If you found this useful, consider giving the repository a star ⭐.
