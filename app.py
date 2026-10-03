from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello!"


@app.route("/healthz")
def healthz():
    return "OK"


@app.route("/notes")
def notes():
    return "Notes"


if __name__ == "__main__":
    app.run()