# ./config/settings.py

from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    app_name: str = Field(alias="APP_NAME")
    app_version: str = Field(alias="APP_VERSION")

    debug: bool = Field(alias="DEBUG")
    environment: str = Field(alias="ENVIRONMENT")

    database_path: Path = Field(alias="DATABASE_PATH")

    log_level: str = Field(alias="LOG_LEVEL")

    request_timeout: int = Field(alias="REQUEST_TIMEOUT")

    user_agent: str = Field(alias="USER_AGENT")

    max_retries: int = Field(alias="MAX_RETRIES")

    request_delay: int = Field(alias="REQUEST_DELAY")

    streamlit_server_port: int = Field(alias="STREAMLIT_SERVER_PORT")

    export_path: Path = Field(alias="EXPORT_PATH")

    cache_path: Path = Field(alias="CACHE_PATH")

    plotly_template: str = Field(alias="PLOTLY_TEMPLATE")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        populate_by_name=True,
    )


settings = Settings()