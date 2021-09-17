class Config:
    """This is the main configuration class that has base configurations for the whole application
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kenmbira:1234@localhost/pitch_arena'

class ProdConfig(Config):
    """This is the class containing the configurations needed for the production environment

    Args:
        Config (class): [This is the parent class for the configurations]
    """
    pass

class DevConfig(Config):
    """This is the class containing the configurations needed for the development environment

    Args:
        Config ([class]): [This is the parent class for the configurations]
    """
    DEBUG = True

class TestConfig(Config):
    """This is the class containing the configurations needed for the testing environment

    Args:
        Config ([class]): [This is the parent class for the configurations]
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kenmbira:1234@localhost/pitch_arena_test'

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}