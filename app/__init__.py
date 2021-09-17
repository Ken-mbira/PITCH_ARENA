from flask import Flask

from config import config_options

def create_app(config_name):
    """This is the app factory, the function that when run initiates the application

    Args:
        config_name ([string]): [This is the name of the configuration environment that the app is running on]
    """

    app = Flask(__name__)

    #Creating the app configurations
    app.config.from_object(config_options[config_name])

    #Initializing the flask extensions

    return app