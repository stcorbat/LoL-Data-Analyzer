from flask import render_template

from app import app, db
from app.forms import SummonerSelect


summoners = db.Table('Summoners', db.metadata, autoload=True, autoload_with=db.engine)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    result = db.session.query(summoners).all()
    form = SummonerSelect()
    form.summoner.choices = [(r.account_id, r.summoner_name) for r in result]
    if form.validate_on_submit():
        pass

    return render_template('index.html', form=form)


@app.route('/about')
def about():
    return render_template('about.html')
