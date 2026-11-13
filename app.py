
import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return os.environ.get("GREETING", "Hello!")


@app.route("/healthz")
def healthz():
    return "OK"


@app.route("/notes")
def notes():
    return "Notes"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
