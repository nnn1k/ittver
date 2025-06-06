from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent


class DbConfig(BaseModel):
    user: str = 'postgres.djompbewvaqavyeforrx'
    password: str = 'ittver'
    host: str = 'aws-0-eu-north-1.pooler.supabase.com'
    port: int = 5432
    name: str = 'postgres'

    @property
    def url(self) -> str:
        return f"postgresql+psycopg://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"


class EmailConfig(BaseModel):
    login: str = 'repost0099@gmail.com'
    password: str = 'rhri isay zltl onia'


class JWTConfig(BaseModel):
    private_key: str = BASE_DIR / 'certs' / 'jwt-private.pem'
    public_key: str = BASE_DIR / 'certs' / 'jwt-public.pem'


class Settings(BaseSettings):
    jwt: JWTConfig = JWTConfig()
    db: DbConfig = DbConfig()
    email: EmailConfig = EmailConfig()


settings = Settings()
