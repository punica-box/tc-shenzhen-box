import os
import json
import binascii

from ontology.ont_sdk import OntologySdk
from ontology.wallet.wallet_manager import WalletManager
from ontology.smart_contract.neo_contract.abi.abi_info import AbiInfo
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

    ROOT_FOLDER = os.path.abspath(basedir)
    WALLET_PATH = os.path.join(ROOT_FOLDER, 'wallet', 'wallet.json')
    CONTRACTS_FOLDER = os.path.join(ROOT_FOLDER, 'contract')
    GAS_LIMIT = 20000000
    GAS_PRICE = 500
    ONT_RPC_ADDRESS = 'http://45.76.243.92:20336'
    CONTRACT_ADDRESS_HEX = ''
    CONTRACT_ADDRESS_BYTEARRAY = bytearray(binascii.a2b_hex(CONTRACT_ADDRESS_HEX))
    CONTRACT_ADDRESS_BYTEARRAY.reverse()
    ONTOLOGY = OntologySdk()
    ONTOLOGY.rpc.set_address(ONT_RPC_ADDRESS)
    with open(os.path.join(CONTRACTS_FOLDER, 'copyright.abi.json')) as f:
        CONTRACT_ABI = json.loads(f.read())
        entry_point = CONTRACT_ABI.get('entrypoint', '')
        functions = CONTRACT_ABI['abi']['functions']
        events = CONTRACT_ABI.get('events', list())
        ABI_INFO = AbiInfo(CONTRACT_ADDRESS_HEX, entry_point, functions, events)
    WALLET_MANAGER = WalletManager()
    WALLET_MANAGER.open_wallet(WALLET_PATH)


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
