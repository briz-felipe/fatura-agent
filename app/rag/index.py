from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from app.config.settings import settings

def create_index(docs):
    embeddings = OllamaEmbeddings(model=settings.EMBED_MODEL)
    vectordb = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=str(settings.DB_DIR)
    )
    return vectordb

def load_index():
    embeddings = OllamaEmbeddings(model=settings.EMBED_MODEL)
    return Chroma(
        persist_directory=str(settings.DB_DIR),
        embedding_function=embeddings
    )
