from flask import Blueprint, json

from ..extensions import flask_db
from ..models import Lotto
from ..datascraper.main import update, lastupdate

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "It's a polish Lottery API, more information coming shortly."

@main.route('/<int:num>')
def lotto_num(num):
    return (flask_db.session.query(Lotto).get(num)).nums

# Updates.
@main.route('/update')
def req_update():    
    res = update()
    return res

@main.route('/lastupdate')
def req_lastupdate():  
    lastupdate()
    return 'Last records updated.'

@main.route('/api/test')
def test():
    return "It works!"