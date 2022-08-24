from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Lotto API"


if __name__ == "__main__":
    app.run()