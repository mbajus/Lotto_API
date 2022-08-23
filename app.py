from unittest import expectedFailure
from urllib import request
from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("lottodb.sqlite")
    except sqlite3.error as e:
        print(e)
    return conn


@app.route('/')
def index():
    return "Lotto API"


if __name__ == "__main__":
    app.run()