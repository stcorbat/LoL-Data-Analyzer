import datetime

from flask import render_template

from app import app, db
from app.forms import QueryForm
from app.scripts import stat_fetcher, champion_parser


summoners = db.Table('Summoners', db.metadata, autoload=True, autoload_with=db.engine)
summoner_matches = db.Table('SummonerMatches', db.metadata, autoload=True, autoload_with=db.engine)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    result = db.session.query(summoners).all()
    form = QueryForm()
    form.summoner.choices = [(r.account_id, r.summoner_name) for r in result]
    if form.validate_on_submit():
        account_id = form.summoner.data

        queue = form.queue.data
        begin_date = form.begin_date.data
        # begin date is an optional field and may not have a value
        if begin_date is None:
            time = 0
        else:
            time = datetime.datetime(year=int(begin_date.year), month=int(begin_date.month), day=int(begin_date.day))\
                .timestamp() * 1000

        stat = form.stat.data

        stat_total = stat_fetcher.get_stat_total(stat, account_id, time, queue)
        if stat in stat_fetcher.by_champion_stats:
            stat_by_champ = stat_fetcher.get_stat_by_champ(stat, account_id, time, queue)

            stat_by_champ_arr = []
            for r in stat_by_champ:
                stat_by_champ_arr.append({
                    'champion': champion_parser.get_champion_name(r.champion),
                    'stat': r.stat,
                    'amount': r.amount
                })
        else:
            stat_by_champ_arr = None

        # these parse the second part of the tuples in the choices that are more human readable
        stat_desc = [item[1] for item in form.stat.choices if item[0] == form.stat.data][0]
        summoner_name = [item[1] for item in form.summoner.choices if item[0] == account_id][0]
    else:
        stat_total = None
        stat_by_champ_arr = None
        stat_desc = None
        summoner_name = None
    return render_template('index.html', form=form, stat_total=stat_total, stat_by_champ=stat_by_champ_arr,
                           stat_desc=stat_desc, summoner_name=summoner_name)


@app.route('/about')
def about():
    return render_template('about.html')
