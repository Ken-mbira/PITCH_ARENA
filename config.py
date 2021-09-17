import os

class Config:
    """This is the main configuration class that has base configurations for the whole application
    """
    pass

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
    pass

class TestConfig(Config):
    """This is the class containing the configurations needed for the testing environment

    Args:
        Config ([class]): [This is the parent class for the configurations]
    """
    pass

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}