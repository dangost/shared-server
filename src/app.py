from flask import Flask

from src.config import Config


def create_app(config: Config) -> Flask:
    _app = Flask("Shared Server")

    """
        Initialize blueprints
    """

    return _app
