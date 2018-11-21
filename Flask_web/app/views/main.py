from flask import Blueprint

main = Blueprint('main',__name__)

@main.route('/index/',methods=['GET','POST'])
def index():
    return '哎哟,不错哦'