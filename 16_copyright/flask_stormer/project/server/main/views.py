from flask import render_template, Blueprint, current_app

main_blueprint = Blueprint('main', __name__,)


@main_blueprint.route('/')
def home():
    # raise RuntimeError("33")
    # current_app.logger.info(
    #     "Home response"
    # )
    return render_template('main/home.html')


@main_blueprint.route("/about")
def about():
    return render_template("main/about.html")
