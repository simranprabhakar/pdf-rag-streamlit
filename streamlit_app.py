import streamlit as st
from utils.pdf_loader import load_pdf
from utils.text_split import split_text
from utils.embedder import embed_texts, model
from utils.vector_store import VectorStore
from utils.llm import ask_local_llm


st.title("Simple RAG Project")
st.write("Upload a PDF → Ask a question → Get AI-powered retrieval")

# Step 1: Upload PDF
pdf = st.file_uploader("Upload PDF", type=["pdf"])

if pdf:
    st.success("PDF uploaded!")

    # Step 2: Extract Text
    text = load_pdf(pdf)
    st.write("### Extracted Text Preview")
    st.write(text[:500])

    # Step 3: Chunking
    chunks = split_text(text)

    # Step 4: Embeddings
    st.write("### Generating Embeddings...")
    embeddings = embed_texts(chunks)

    # Step 5: Store in Vector DB
    db = VectorStore()
    db.add(embeddings, chunks)

    st.success("Vector Database Ready!")

    # Step 6: Ask Question
    question = st.text_input("Ask a question about the PDF")

    if question:
        query_embedding = model.encode([question])[0]
        results = db.search(query_embedding)

        st.write("## 🔍 Retrieved Answer")
        context = "\n\n".join(results)
        final_answer = ask_local_llm(question, context)

        st.write("## 🧠 LLM Final Answer")
        st.write(final_answer)
