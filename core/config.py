from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str = f"postgresql+asyncpg://postgres:root@"
    db_echo: bool = True


settings = Settings()
