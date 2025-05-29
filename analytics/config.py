from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    HOST: str
    PORT: int

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


config = Settings()
