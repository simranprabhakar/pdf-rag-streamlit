from langchain_community.document_loaders import PyMuPDFLoader
import tempfile

def load_pdf(uploaded_file):
    # Save uploaded file temporarily so PyMuPDFLoader can read it
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    loader = PyMuPDFLoader(tmp_path)
    docs = loader.load()

    # Combine pages into one string
    full_text = "\n".join([d.page_content for d in docs])
    return full_text


