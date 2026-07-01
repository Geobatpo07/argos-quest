# ./config/settings.py

from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # ------------------------------------------------------------------
    # Application
    # ------------------------------------------------------------------

    app_name: str = Field(
        default="Argos Quest",
        alias="APP_NAME",
    )

    app_version: str = Field(
        default="0.1.0",
        alias="APP_VERSION",
    )

    debug: bool = Field(
        default=False,
        alias="DEBUG",
    )

    environment: str = Field(
        default="production",
        alias="ENVIRONMENT",
    )

    # ------------------------------------------------------------------
    # Database
    # ------------------------------------------------------------------

    database_path: Path = Field(
        default=Path("data/argos.duckdb"),
        alias="DATABASE_PATH",
    )

    # ------------------------------------------------------------------
    # Logging
    # ------------------------------------------------------------------

    log_level: str = Field(
        default="INFO",
        alias="LOG_LEVEL",
    )

    # ------------------------------------------------------------------
    # HTTP
    # ------------------------------------------------------------------

    request_timeout: int = Field(
        default=30,
        alias="REQUEST_TIMEOUT",
    )

    user_agent: str = Field(
        default="ArgosQuest",
        alias="USER_AGENT",
    )

    max_retries: int = Field(
        default=3,
        alias="MAX_RETRIES",
    )

    request_delay: int = Field(
        default=2,
        alias="REQUEST_DELAY",
    )

    # ------------------------------------------------------------------
    # Streamlit
    # ------------------------------------------------------------------

    streamlit_server_port: int = Field(
        default=8501,
        alias="STREAMLIT_SERVER_PORT",
    )

    # ------------------------------------------------------------------
    # Paths
    # ------------------------------------------------------------------

    export_path: Path = Field(
        default=Path("exports"),
        alias="EXPORT_PATH",
    )

    cache_path: Path = Field(
        default=Path("cache"),
        alias="CACHE_PATH",
    )

    # ------------------------------------------------------------------
    # Plotly
    # ------------------------------------------------------------------

    plotly_template: str = Field(
        default="plotly_white",
        alias="PLOTLY_TEMPLATE",
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()