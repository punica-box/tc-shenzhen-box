import os
from flask import Flask, render_template
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
# from flask_debugtoolbar import DebugToolbarExtension
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis


app = Flask(
    __name__,
    template_folder='../client/templates',
    static_folder='../client/static'
)

app_settings = os.getenv('APP_SETTINGS', 'project.server.config.DevelopmentConfig')
app.config.from_object(app_settings)

# login_manager
lm = LoginManager()
lm.init_app(app)

# sqlalchemy
db = SQLAlchemy(app)
setattr(app, 'db', db)

# Redis
redis_store = FlaskRedis(decode_responses=True)
redis_store.init_app(app)
app.redis = app.extensions['redis']

# other extension
bcrypt = Bcrypt(app)
# toolbar = DebugToolbarExtension(app)
bootstrap = Bootstrap(app)


# from project.server.user.views import user_blueprint
from project.server.main.views import main_blueprint
from project.server.api import api as testapi


def regist_routes(app, bls):
    """routes registed."""
    map(app.register_blueprint, bls)


# Attach blueprints
regist_routes(app, [main_blueprint, testapi])


from project.server.models import User

lm.login_view = "user.login"
lm.login_message_category = 'danger'


@lm.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()


# error handlers

@app.errorhandler(401)
def unauthorized_page(error):
    return render_template("errors/401.html"), 401


@app.errorhandler(403)
def forbidden_page(error):
    return render_template("errors/403.html"), 403


@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404


@app.errorhandler(500)
def server_error_page(error):
    return render_template("errors/500.html"), 500
