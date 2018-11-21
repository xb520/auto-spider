from flask import Flask,render_template
from app.config import config
from app.extensions import config_extensions
from .views import config_blueprint

# 自定义错误页面
def config_errorhandler(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html')
# 封装一个方法，专门用于创建Flask实例
def create_app(config_name):
    # 创建应用实例
    app = Flask(__name__)
    # 初始化配置
    app.config.from_object(config.get(config_name, 'default'))
    # 调用初始化函数
    config[config_name].init_app(app)
    # 返回应用实例
    config_extensions(app)
    #注册蓝本
    config_blueprint(app)
    # 调用错误页面
    config_errorhandler(app)

    return app