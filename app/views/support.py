from flask import Blueprint, request
from flask_cors import CORS
import controllers.support_controller as controller

app = Blueprint('support', __name__)
CORS(app)


@app.route("/support", methods=["GET", "POST"])
def support():
    if request.method == "GET":
        return controller.retrieve_support_request()

    if request.method == "POST":
        return controller.save_support_request(request.json)
