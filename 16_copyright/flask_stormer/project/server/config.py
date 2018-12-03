import os
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    """Base configuration."""
    SECRET_KEY = 'd5bacbc0e4b77d048527c51eddb9b930f97ee'
    DEBUG = False
    TESTING = False
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    redis_url = "redis://127.0.0.1:6379/0"

    # flask-mail config
    MAIL_SERVER = 'smtp.exmail.qq.com'
    MAIL_PROT = 25
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = MAIL_DEFAULT_SENDER = ""
    MAIL_PASSWORD = ""
    MAIL_DEBUG = False
    MAIL_SUPPRESS_SEND = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.sqlite')
    DEBUG_TB_ENABLED = True
    MAIL_DEBUG = True


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'
    DEBUG_TB_ENABLED = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    """Production configuration."""
    # if not os.getenv('MYSQL_PWD'):
    #     raise RuntimeError("Set 'MYSQL_PWD' to enviroment first")
    SECRET_KEY = 'my_preciousd5bacbc0e4b77d048527c51eddb9b930f97ee'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@localhost:3306/%s' % (
        "root", os.getenv('MYSQL_PWD'), "pro")
    DEBUG_TB_ENABLED = False
