from flask import Blueprint, jsonify, make_response, json

from ..extensions import flask_db
from ..models import Lotto

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "It's a polish Lottery API, more information coming shortly."

@main.route('/api/lotto/id/<int:num>')
def lotto_num(num):
    try:
        return jsonify(flask_db.session.query(Lotto).get(num).obj_to_dict())
    except:
        return custom_error("No result found on requested ID.", 404)

@main.route('/api/lotto/date/<int:date>')
def lotto_date(date):
    if len(str(date)) == 8:
        try:
            return jsonify(flask_db.session.query(Lotto).filter_by(date=date).first().obj_to_dict())
        except:
            return custom_error("No result found on requested date.", 404)
    else:
        return custom_error("Invalid data type. Use YYYYMMDD.", 400)

def custom_error(message, status_code):
    res = {"code": status_code, "message": message}
    return make_response(jsonify(res), status_code)