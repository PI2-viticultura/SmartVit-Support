from flask import Blueprint, request, jsonify
from flask_cors import CORS
from extensions import db
import requests

app = Blueprint('hello', __name__)
CORS(app)

@app.route("/", methods=["GET"])
def hello():
    return "Hello World !", 200