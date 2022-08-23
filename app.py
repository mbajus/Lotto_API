from unittest import expectedFailure
from urllib import request
from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return "Lotto API"


if __name__ == "__main__":
    app.run()