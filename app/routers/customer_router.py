from app import app
from app.controllers import customer_controller
from flask import Blueprint, request

customer_blueprint = Blueprint('customer_router', __name__)

@app.route("/users", methods = ['GET'])
def showUsers():
    return customer_controller.shows()

@app.route("/user", methods = ['GET'])
def showUser():
    params = request.json
    return customer_controller.show(**params)

@app.route("/user/insert", methods = ['POST'])
def insertUsers():
    params = request.json
    return customer_controller.insert(*params)

@app.route("/user/update", methods = ['POST'])
def updateUsers():
    params = request.json
    return customer_controller.update(**params)

@app.route("/user/delete", methods = ['POST'])
def deleteUsers():
    params = request.json
    return customer_controller.delete(**params)

@app.route("/user/token", methods = ['GET'])
def requestToken():
    params = request.json
    return customer_controller.token(**params)

