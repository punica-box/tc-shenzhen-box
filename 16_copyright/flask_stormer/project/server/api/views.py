from flask import request, jsonify
from flask.views import MethodView


class Test(MethodView):
    methods = ['GET']

    def get(self):
        return jsonify({"test": "test"})


def add_urls(blueprint, prefix=''):
    blueprint.add_url_rule(
        rule='/test',
        view_func=Test.as_view('test')
    )
