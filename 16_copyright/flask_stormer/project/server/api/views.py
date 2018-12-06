from flask import request, jsonify
from flask.views import MethodView
from .forms import CopyrightForm
from flask import current_app as app
from project.server.helpers.cnt_util import create_copyright_to_contract


class CreateCopyright(MethodView):
    methods = ['POST']

    def post(self):
        form = CopyrightForm(request.form)
        if form.validate_on_submit():
            default_identity_account = app.config['WALLET_MANAGER'].get_account(
                form.ont_id.data, form.password.data)
            tx_hash = create_copyright_to_contract(
                default_identity_account, form.copyright_hash.data)
            return jsonify({"code": 0, "msg": "success", "data": tx_hash})
        elif form.errors:
            return jsonify({"code": 1, "msg": "error parameters"})


def add_urls(blueprint, prefix=''):

    blueprint.add_url_rule(
        rule='/copyright',
        view_func=CreateCopyright.as_view('create-copyright')
    )
