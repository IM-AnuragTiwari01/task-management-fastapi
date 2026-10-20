from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(extra="ignore")
    DB_CONNECTION: str = "mysql+pymysql://mysql:mysql@mysql_db:3306/mydb" # pydantics checks the environment variables provided by docker firrst if None were provided it fall back to your default string

settings = Settings()

# print(settings.DB_CONNECTION)