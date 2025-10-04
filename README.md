# fatura-agent

Agente de IA para análise de faturas em PDF usando RAG (Retrieval-Augmented Generation) com LLaMA local.

## 📋 Pré-requisitos

- Python 3.8+
- [Ollama](https://ollama.ai/) instalado
- Modelos LLaMA baixados no Ollama

## 🚀 Instalação

### 1. Clone o repositório
```bash
git clone <url-do-repositorio>
cd fatura-agent
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Configure o Ollama
```bash
# Baixe os modelos necessários
ollama pull llama3.1:8b
ollama pull mxbai-embed-large
```

### 4. Adicione seus PDFs
Coloque os arquivos PDF na pasta `input/`:
```bash
cp suas-faturas.pdf input/
```

## 💻 Como usar

### 1. Indexar os PDFs
Primeiro, crie o índice dos documentos:
```bash
python main_index.py
```

### 2. Iniciar o chat
Depois execute o chat interativo:
```bash
python main_chat.py
```

### Exemplo de uso
```
💬 Chat com seus PDFs (digite 'sair' para encerrar)

[Pergunta] -> Qual o valor total da fatura?
[Resposta] -> O valor total da fatura é R$ 1.234,56
Duração: 0:00:03.245

[Pergunta] -> Quais foram as principais despesas?
[Resposta] -> As principais despesas foram...

[Pergunta] -> sair
```

## ⚙️ Configuração

Edite `app/config/settings.py` para ajustar:
- Modelo LLM: `LLM_MODEL = "llama3.1:8b"`
- Modelo de embedding: `EMBED_MODEL = "mxbai-embed-large"`
- Diretórios de entrada e banco de dados

## 📁 Estrutura do projeto

```
fatura-agent/
├── app/
│   ├── config/settings.py    # Configurações
│   ├── loaders/pdf_loader.py # Carregamento de PDFs
│   └── rag/
│       ├── index.py          # Criação do índice
│       └── query.py          # Consultas RAG
├── input/                    # PDFs para análise
├── db/                       # Banco vetorial (ChromaDB)
├── main_index.py            # Script de indexação
├── main_chat.py             # Chat interativo
└── requirements.txt         # Dependências
```

## 🔧 Solução de problemas

**Erro de modelo não encontrado:**
```bash
ollama list  # Verifique modelos instalados
ollama pull llama3.1:8b  # Baixe se necessário
```

**Erro de dependências:**
```bash
pip install --upgrade -r requirements.txt
```

**PDFs não encontrados:**
- Verifique se os arquivos estão na pasta `input/`
- Execute `python main_index.py` novamente