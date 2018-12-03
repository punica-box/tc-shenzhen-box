from flask import current_app
from werkzeug.local import LocalProxy


def __get_redis():
    return current_app.redis


redis_store = LocalProxy(__get_redis)
