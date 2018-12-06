from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length


class CopyrightForm(FlaskForm):
    ont_id = StringField('Ont_id', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    copyright_hash = StringField('Copyright_hash', [DataRequired(), Length(max=36)])
