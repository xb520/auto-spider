from flask_script import Manager
from app import create_app
import os
from flask_migrate import MigrateCommand



# 获取配置
config_name = os.environ.get('FLASK_CONFIG') or 'default'
app = create_app(config_name)
manager = Manager(app)

# 配置迁移
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()