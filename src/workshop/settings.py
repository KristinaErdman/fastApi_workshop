from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    database_url: str = "postgresql://user:password@postgresserver/db"
    jwt_secret: str
    jwt_algorithm: str = 'HS256'
    jwt_expiration: int = 3600  # (sec)


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8'
)
