from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_and_split_pdfs(input_dir):
    """Carrega PDFs da pasta e divide em chunks"""
    docs = []
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)

    for pdf_path in input_dir.glob("*.pdf"):
        loader = PyPDFLoader(str(pdf_path))
        pages = loader.load()
        chunks = splitter.split_documents(pages)
        docs.extend(chunks)
    
    return docs
