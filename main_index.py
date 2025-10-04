from app.loaders.pdf_loader import load_and_split_pdfs
from app.rag.index import create_index
from app.config.settings import settings

if __name__ == "__main__":
    print("📥 Carregando PDFs e criando índice...")
    docs = load_and_split_pdfs(settings.INPUT_DIR)
    create_index(docs)
    print("✅ Índice criado e salvo em /db")
