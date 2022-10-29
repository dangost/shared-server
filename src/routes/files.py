from flask import Blueprint

files_controller = Blueprint("files_controller", __name__,  url_prefix="/files")


@files_controller.route("/")
def all_files():
    pass


@files_controller.route('/<filename>', methods=['GET'])
def download_file():
    pass
