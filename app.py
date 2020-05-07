import os
import dataset

from datetime import datetime
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DB_DSN = os.getenv("DATABASE_URL", "sqlite:///data.db")
db = dataset.connect(DB_DSN)


@app.route("/api")
def index():
    table = db["events"]
    records = table.all()
    return jsonify(list(records))


@app.before_request
def log_access():
    table = db["events"]
    table.insert({
        "event": "request",
        "at": datetime.now()
    })


@app.before_first_request
def init_db():
    table = db["events"]
    table.insert({
        "event": "bootstrap",
        "at": datetime.now()
    })
