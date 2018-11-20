from flask import Blueprint
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return '终于见到你'