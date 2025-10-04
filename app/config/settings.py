
# config.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

class Settings(BaseSettings):
    """
    Carrega e valida as configurações da aplicação a partir de variáveis de ambiente.
    """
    
    # Modelo para carregar variáveis de um arquivo .env, se existir (útil para desenvolvimento local)
    # Para produção, as variáveis serão lidas diretamente do ambiente (export).
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')
    BASE_DIR:Path = Path(__file__).resolve().parent.parent.parent

    # Caminhos
    INPUT_DIR:Path = BASE_DIR / "input"
    DB_DIR:Path = BASE_DIR / "db"

    # Modelos
    LLM_MODEL:str = "llama3.1:8b"
    # LLM_MODEL:str = "llama3.2:1b"
    # EMBED_MODEL:str = "nomic-embed-text"
    # EMBED_MODEL = "snowflake-arctic-embed" #melhor para pt-bt
    EMBED_MODEL:str = "mxbai-embed-large"




# Instância única que será importada em outros módulos da sua aplicação
settings = Settings()