from flask import Blueprint, json

from ..extensions import db
from ..models import Lotto
from ..datascraper.main import update, lastupdate

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "It's a polish Lottery API, more information coming shortly."


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