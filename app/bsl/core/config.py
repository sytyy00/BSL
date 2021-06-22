from typing import Any, Dict, Optional

from pydantic import BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    API_V1_STR: str = "/api"
    DEBUG: bool
    PROJECT_NAME: str
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    BACKEND_URL: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None
    REDIS_PASSWORD: str
    REDIS_HOST: str
    REDIS_URL: Optional[str] = None

    class Config:
        env_file = "/home/sytyy00/up_project/bsl/.env"

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    @validator("REDIS_URL", pre=True)
    def assemble_redis_connection(cls, v: Optional[str], values: Dict[str, Any]) -> str:
        if isinstance(v, str):
            return v

        return f"redis://:{values.get('REDIS_PASSWORD')}@{values.get('REDIS_HOST')}:6379/0"

    class Config:
        case_sensitive = True


settings = Settings(_env_file='/home/sytyy00/up_project/bsl/.env')
