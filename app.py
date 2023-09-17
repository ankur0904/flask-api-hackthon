from flask import Flask, jsonify
from data import data

app = Flask(__name__)


@app.route('/')
def hello():
    # return 'Hello, World!'
    return jsonify(data)