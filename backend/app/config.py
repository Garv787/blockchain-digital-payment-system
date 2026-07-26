from __future__ import annotations

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    # App
    environment: str = Field("development", alias="ENVIRONMENT")
    log_level: str = Field("INFO", alias="LOG_LEVEL")
    cors_origins: str = Field("http://localhost:5173", alias="CORS_ORIGINS")

    # JWT
    jwt_secret_key: str = Field("change_me", alias="JWT_SECRET_KEY")
    jwt_algorithm: str = Field("HS256", alias="JWT_ALGORITHM")
    access_token_expire_minutes: int = Field(15, alias="ACCESS_TOKEN_EXPIRE_MINUTES")
    refresh_token_expire_days: int = Field(7, alias="REFRESH_TOKEN_EXPIRE_DAYS")

    # Database
    database_url: str = Field(
        "sqlite:///./payment_system.db",
        alias="DATABASE_URL",
    )

    # Blockchain
    sepolia_rpc_url: str | None = Field(None, alias="SEPOLIA_RPC_URL")
    blockchain_contract_address: str | None = Field(None, alias="CONTRACT_ADDRESS")
    blockchain_contract_abi_path: str | None = Field(None, alias="CONTRACT_ABI_PATH")
    wallet_private_key: str | None = Field(None, alias="PRIVATE_KEY")


settings = Settings()