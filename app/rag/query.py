from langchain.chains import RetrievalQA
from langchain_ollama import ChatOllama
from app.config.settings import settings
from .index import load_index

# Cache global para reutilizar componentes
_vectordb = None
_qa_chain = None

def _get_qa_chain():
    """Retorna chain reutilizável"""
    global _vectordb, _qa_chain
    
    if _qa_chain is None:
        _vectordb = load_index()
        retriever = _vectordb.as_retriever(search_kwargs={"k": 5})
        
        llm = ChatOllama(
            model=settings.LLM_MODEL,
            temperature=0.1,
            num_predict=512,
            top_p=0.9,
            num_ctx=4096
        )
        
        from langchain.prompts import PromptTemplate
        
        prompt_template = """
        Você é um assistente especializado em analisar documentos PDF. 
        Use APENAS as informações dos documentos fornecidos para responder.
        Se não souber a resposta baseada nos documentos, diga "Não encontrei essa informação nos documentos".
        
        Contexto dos documentos:
        {context}
        
        Pergunta: {question}
        
        Resposta detalhada:
        """
        
        prompt = PromptTemplate(
            template=prompt_template,
            input_variables=["context", "question"]
        )
        
        _qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            return_source_documents=False,
            chain_type_kwargs={"prompt": prompt}
        )
    
    return _qa_chain

def run_query(question: str):
    """Executa pergunta no índice com LLaMA"""
    qa = _get_qa_chain()
    result = qa.invoke({"query": question})
    return result["result"]
