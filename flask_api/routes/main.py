from flask import Blueprint, request

from flask_api.extensions import db
from flask_api.models import Lotto
from flask_api.datascraper.scraper import initialdb

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
    initialdb()
    return "DONE"
