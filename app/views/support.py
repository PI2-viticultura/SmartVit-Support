from flask import Blueprint, request, jsonify
from flask_cors import CORS
from extensions import db
import controllers.support_controller as controller
import requests

app = Blueprint('support', __name__)
CORS(app)

@app.route("/support", methods=["POST"])
def support():
    return controller.save_support_request(request.json)