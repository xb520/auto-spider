from .main import main
from .users import users

# 蓝本配置
DEFAULT_BLUEPRINT = (
    (main, ''),
    (users,'/users')
)

# 封装函数，完成蓝本注册
def config_blueprint(app):
    for blueprint, prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=prefix)