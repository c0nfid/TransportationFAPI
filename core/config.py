import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    db_url: str = f"{os.environ.get('DB_ADDRESS')}"
    db_echo: bool = True


settings = Settings()
