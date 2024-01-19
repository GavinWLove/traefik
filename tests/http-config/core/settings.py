# import logging
from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseSettings, validator, AnyUrl


class AppSettings(BaseSettings):
    docs_url: str = "/docs"
    openapi_prefix: str = ""
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    title: str = "社区助手-意图识别Service"
    version: str = "0.0.1"

    api_prefix: str = "/api"
    allowed_hosts: List[str] = ["*"]

    LOG_LEVEL: str

    # OPENAI_API_KEY: str
    # OPENAI_API_BASE: str

    VECTOR_DB_HOST: str
    VECTOR_DB_PORT: str
    VECTOR_COLLECTION_NAME: str
    VECTOR_EMBEDDING_MODEL: str

    VECTOR_COLLECTION_FAQ_NAME: str = "intention_faq"
    VECTOR_COLLECTION_TASK_NAME: str = "intention_task"

    SERVICE_AGENT_URL: str

    VOLC_ACCESS_KEY: str
    VOLC_SECRET_KEY: str
    VOLC_HOST: str
    VOLC_REGION: str

    REDIS_DATABASE: str
    REDIS_HOST: str
    REDIS_PORT: str
    REDIS_PWD: str
    REDIS_DB_URI: Optional[AnyUrl] = None

    @validator("REDIS_DB_URI", pre=True)
    def redis_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return f'redis://{values.get("REDIS_HOST")}:{values.get("REDIS_PORT")}'
        # return f'redis://:{values.get("REDIS_PWD")}@{values.get("REDIS_HOST")}:{values.get("REDIS_PORT")}/{values.get("REDIS_DATABASE")}'

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {
            "debug": True if self.LOG_LEVEL == "DEBUG" else False,
            "docs_url": self.docs_url,
            "openapi_prefix": self.openapi_prefix,
            "openapi_url": self.openapi_url,
            "redoc_url": self.redoc_url,
            "title": self.title,
            "version": self.version,
        }


settings = AppSettings(_env_file=".env")
