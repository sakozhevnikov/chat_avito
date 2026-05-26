import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    TELEGRAM_BOT_TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN")
    POSTGRES_DSN: str = os.getenv("POSTGRES_DSN")
    OLLAMA_URL: str = os.getenv("OLLAMA_URL", "http://localhost:11434")
    MODEL_NAME: str = os.getenv("MODEL_NAME", "qwen2.5:0.5b")

settings = Settings()