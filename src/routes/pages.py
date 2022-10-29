from flask import Blueprint, render_template, redirect

pages_controller = Blueprint("pages_controller", __name__)


@pages_controller.route('/', methods=['GET'])
def main_page():
    return redirect('/files')
