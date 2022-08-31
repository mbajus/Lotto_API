from flask import Blueprint, request

from flask_api.extensions import db
from flask_api.models import Lotto
from flask_api.datascraper.htmltool import gethtml

main = Blueprint('main', __name__)

@main.route('/')
def index():
    dball = Lotto.query.all()

    return dball

@main.route('/add', methods=['POST'])
def add():
    content_type = request.headers.get('Content-Type')
    print("TYP POST", content_type)
    if (content_type == 'application/json'):
        json = request.json
        return json
    else:
        return 'Content-Type not supported!'

@main.route('/init')
def init():
    
    return gethtml("https://www.lotto.pl/lotto/wyniki-i-wygrane/date,1957-08-29,10")
