import os
import re

class Config:
    """This is the main configuration class that has base configurations for the whole application
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    """This is the class containing the configurations needed for the production environment

    Args:
        Config (class): [This is the parent class for the configurations]
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    """This is the class containing the configurations needed for the development environment

    Args:
        Config ([class]): [This is the parent class for the configurations]
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kenmbira:1234@localhost/pitch_arena'

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