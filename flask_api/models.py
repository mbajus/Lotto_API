from .extensions import db 

class Lotto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nums = db.Column(db.Text)
    numsp = db.Column(db.Text)
    date = db.Column(db.Integer)
    time = db.Column(db.Integer)