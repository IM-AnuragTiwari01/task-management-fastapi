from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra="ignore")
    DB_CONNECTION: str  # pydantics checks the environment variables provided by docker firrst if None were provided it fall back to your default string

settings = Settings()

# print(settings.DB_CONNECTION)