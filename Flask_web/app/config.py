import os
import pymysql
from flask_sqlalchemy import SQLAlchemy

base_dir =  os.path.abspath(os.path.dirname(__file__))

# 通用配置
class Config:
    # 秘钥
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123456'
    # 数据库
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 邮件发送
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.1000phone.com'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'xuke@1000phone.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or '123456'

    # 额外的初始化操作
    @staticmethod
    def init_app(app):
        pass


# 开发环境
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Root&123456@192.168.9.105/mediatest2'


# 测试环境
class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir,
   	                                                          'blog-test.sqlite')
# 生产环境
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir,
                                                                    'blog.sqlite')


config = {
   	    'development': DevelopmentConfig,
   	    'testing': TestingConfig,
   	    'production': ProductionConfig,
   	    'default': DevelopmentConfig
   	}