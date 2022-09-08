from flask import Blueprint, json

from ..extensions import flask_db
from ..models import Lotto
from ..datascraper.main import update, lastupdate

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "It's a polish Lottery API, more information coming shortly."

@main.route('/api/lotto/id/<int:num>')
def lotto_num(num):
    return (flask_db.session.query(Lotto).get(num)).nums

@main.route('/api/lotto/date/<int:date>')
def lotto_date(date):
    if len(str(date)) == 8:
        possible_dates = flask_db.session.query(Lotto).with_entities(Lotto.date).all()
        for p_date in possible_dates:
            if p_date[0] == date:
                return flask_db.session.query(Lotto).filter_by(date=date).first().nums
        else:
            return f"There wasn't any lottery draw on {date}"
    else:
        return "Incorect data format, use YYYYMMDD."

@main.route('/api/test')
def test():
    return "It works!"