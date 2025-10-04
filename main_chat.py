from app.rag.query import run_query
from datetime import datetime

if __name__ == "__main__":
    print("\n💬 Chat com seus PDFs (digite 'sair' para encerrar)")
    while True:
        q = input("\n[Pergunta] -> ")
        start = datetime.now()
        if q.lower() in ["sair", "exit", "quit"]:
            break
        answer = run_query(q)
        end = datetime.now()
        duration = end - start
        print("[Resposta] -> ", answer,f"\nDuração:{duration}")