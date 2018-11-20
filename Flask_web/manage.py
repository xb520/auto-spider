from flask_script import Manager
from Flask_web.app import app

manager = Manager(app)

if __name__ == '__main__':
    manager.run()