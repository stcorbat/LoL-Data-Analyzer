from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired


class SummonerSelect(FlaskForm):
    summoner = SelectField('Summoner', coerce=str, validators=[DataRequired()])
    submit = SubmitField('Submit')
