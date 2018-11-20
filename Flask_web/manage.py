from flask_script import Manager
from Flask_web.app import create_app
import os



# 获取配置
config_name = os.environ.get('FLASK_CONFIG') or 'default'
app = create_app(config_name)
manager = Manager(app)

if __name__ == '__main__':
    manager.run()