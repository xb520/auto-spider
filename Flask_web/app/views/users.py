from flask import Blueprint, render_template, flash, current_app, redirect, url_for, request, jsonify
# from app.forms import RegisterForm, LoginForm, ChangePasswordForm, IconForm, ResetPassword, ResetForm
# from app.models import User
# from app.extensions import db
# from app.email import send_mail
# from flask_login import login_user, logout_user, login_required, current_user
# from app.extensions import photos
import os

# 生成蓝本
users = Blueprint('users', __name__)


# 第一个视图函数
@users.route('/register/', methods=['GET', 'POST'])
def register():

    return render_template('users/hello.html',)