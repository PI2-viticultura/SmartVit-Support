from flask import Blueprint
from flask_cors import CORS


app = Blueprint('hello', __name__)
CORS(app)


@app.route("/", methods=["GET"])
def hello():
    return "Hello World !", 200
