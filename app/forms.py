from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, DateField
from wtforms.validators import Optional


# queue ids are pulled from the queues.json on riots developer site
queue_types = [
    (400, 'Normal Draft'),
    (420, 'Ranked Solo/Duo'),
    (430, 'Normal Blind'),
    (440, 'Ranked Flex'),
    (450, 'ARAM'),
    (700, 'Clash'),
    (900, 'URF'),
    (1020, 'One for All')
]

stats = [
    ('cspm', 'CS/min'),
    ('win_rate', 'Win Rate'),
    ('kda', 'KDA'),
    ('vision_score', 'Vision Score')
]

filters = [
    ('recent', 'Most Recent'),
    ('oldest', 'Oldest')
]


class QueryForm(FlaskForm):
    summoner = SelectField('Summoner', coerce=str)
    begin_date = DateField('Begin Date', format='%m/%d/%Y', validators=[Optional()])
    queue = SelectField('Queue Type', choices=queue_types, coerce=int)
    stat = SelectField('Statistic', choices=stats, coerce=str)
    filter = SelectField('Filter', choices=filters, coerce=str)
    submit = SubmitField('Submit')

