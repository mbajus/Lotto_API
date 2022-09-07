from flask import Blueprint, request

from flask_api.extensions import db
from flask_api.models import Lotto
from datascraper.main import update

main = Blueprint('main', __name__)

@main.route('/')
def index():
    dball = Lotto.query.all()
    print(dball)
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
    
    return "XD"

# Updates.
@main.route('/update')
def req_update():    
    update()
    return 'Update done.'

@main.route('/lastupdate')
def req_lastupdate():  

    return 'Update done.'

@main.route('/api/test')
def test():
    return "It works!"