from pydantic import BaseSettings

class Settings(BaseSettings):
    mysql_user: str
    mysql_password: str
    mysql_db: str
    mysql_host: str
    secret_key: str
    algorithm: str
    access_token_expiry_minutes: int

    class Config:
        env_file = ".env"

settings = Settings()