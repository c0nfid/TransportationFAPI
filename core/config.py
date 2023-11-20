from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str = f"postgresql+asyncpg://postgres:root@26.67.142.41:5432/Autopark"
    db_echo: bool = True


settings = Settings()
