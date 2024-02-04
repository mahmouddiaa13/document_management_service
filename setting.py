import pydantic_settings


class BaseSettings(pydantic_settings.BaseSettings):
    class Config:
        env_file = ".env"


class DBSettings(BaseSettings):
    TYPE: str = ""
    HOST: str = ""
    PORT: int
    INDEX_NAME: str = ""
    USERNAME: str = ""
    PWD: str = ""

    class Config(BaseSettings.Config):
        env_prefix = "DB_"


class DBTestingSettings(DBSettings):
    TYPE: str = ""
    HOST: str = ""
    PORT: int
    INDEX_NAME: str = ""
    USERNAME: str = ""
    PWD: str = ""

    class Config(BaseSettings.Config):
        env_prefix = "DB_TESTING_"


class OperationSettings(BaseSettings):
    MODE: str = "dev"

    class Config(BaseSettings.Config):
        env_prefix = "OPERATION_"


db_settings = DBSettings()
testing_db_settings = DBTestingSettings()
operation_settings = OperationSettings()


def get_db_settings() -> DBSettings:
    if operation_settings.MODE == "dev":
        return db_settings
    return testing_db_settings
