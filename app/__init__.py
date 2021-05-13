from flask import Flask
from config import Config
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config.from_object(Config)
jwt = JWTManager(app)

from app.routers.customer_router import *


app.register_blueprint(customer_blueprint)
