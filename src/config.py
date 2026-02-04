"""Configuration management for Straker Verify Dashboard."""

import os
from pathlib import Path
from typing import Optional

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Required settings
    straker_verify_api_key: str = Field(
        ...,
        description="Straker Verify API key",
        alias="STRAKER_VERIFY_API_KEY",
    )

    # Optional API settings
    straker_verify_base_url: str = Field(
        default="https://api-verify.straker.ai",
        description="Straker Verify API base URL",
        alias="STRAKER_VERIFY_BASE_URL",
    )

    # Language settings
    default_source_language: str = Field(
        default="en",
        description="Default source language code",
        alias="DEFAULT_SOURCE_LANGUAGE",
    )
    default_target_language: str = Field(
        default="es",
        description="Default target language code",
        alias="DEFAULT_TARGET_LANGUAGE",
    )

    # Cache settings
    cache_enabled: bool = Field(
        default=True,
        description="Enable caching",
        alias="CACHE_ENABLED",
    )
    cache_ttl: int = Field(
        default=3600,
        description="Cache TTL in seconds",
        alias="CACHE_TTL",
    )

    # Logging settings
    log_level: str = Field(
        default="INFO",
        description="Logging level",
        alias="LOG_LEVEL",
    )
    log_file: Optional[str] = Field(
        default="straker_verify_dashboard.log",
        description="Log file path",
        alias="LOG_FILE",
    )

    # UI settings
    theme: str = Field(
        default="dark",
        description="UI theme (dark/light)",
        alias="THEME",
    )
    auto_refresh_interval: int = Field(
        default=5,
        description="Auto-refresh interval in seconds",
        alias="AUTO_REFRESH_INTERVAL",
    )

    @field_validator("log_level")
    @classmethod
    def validate_log_level(cls, v: str) -> str:
        """Validate log level."""
        valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        v_upper = v.upper()
        if v_upper not in valid_levels:
            raise ValueError(f"Invalid log level. Must be one of: {valid_levels}")
        return v_upper

    @field_validator("theme")
    @classmethod
    def validate_theme(cls, v: str) -> str:
        """Validate theme."""
        valid_themes = ["dark", "light"]
        v_lower = v.lower()
        if v_lower not in valid_themes:
            raise ValueError(f"Invalid theme. Must be one of: {valid_themes}")
        return v_lower

    @field_validator("auto_refresh_interval")
    @classmethod
    def validate_refresh_interval(cls, v: int) -> int:
        """Validate auto-refresh interval."""
        if v < 1:
            raise ValueError("Auto-refresh interval must be at least 1 second")
        if v > 300:
            raise ValueError("Auto-refresh interval must be at most 300 seconds")
        return v


def get_settings() -> Settings:
    """Get application settings.
    
    Returns:
        Settings: Application settings instance
        
    Raises:
        ValueError: If required settings are missing or invalid
    """
    try:
        return Settings()
    except Exception as e:
        # Provide helpful error message if .env file is missing
        env_file = Path(".env")
        if not env_file.exists():
            raise ValueError(
                "Configuration file '.env' not found. "
                "Please copy '.env.example' to '.env' and configure your API key."
            ) from e
        raise


# Global settings instance
settings: Optional[Settings] = None


def init_settings() -> Settings:
    """Initialize global settings instance.
    
    Returns:
        Settings: Initialized settings instance
    """
    global settings
    if settings is None:
        settings = get_settings()
    return settings


def get_app_settings() -> Settings:
    """Get the global settings instance.
    
    Returns:
        Settings: Global settings instance
        
    Raises:
        RuntimeError: If settings have not been initialized
    """
    if settings is None:
        raise RuntimeError(
            "Settings not initialized. Call init_settings() first."
        )
    return settings