from flask import Flask

from src.routes.files import files_controller
from src.routes.pages import pages_controller


def init_blueprints(_app: Flask) -> None:
    """
    :param _app: _app - Flask app instance
    :return: None - _app get by reference, so we needn't return it
    """
    _app.register_blueprint(pages_controller)
    _app.register_blueprint(files_controller)
