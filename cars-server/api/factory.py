from flask import Flask
from flask_cors import CORS

from flask_pymongo import PyMongo
from flask_restful import Api

from api.controller.car import Car
from api.controller.car import CarList

app = Flask(__name__)

# Configure CORS
cors = CORS(app,  origins=['http://localhost:8080'])

# Configure database
app.config["MONGO_URI"] = "mongodb://3.14.7.212:27017/Cars"
app.database = PyMongo(app)
app.cars_collection = app.database.db.cars

# Create api
api = Api(app)

api.add_resource(Car, '/car', '/car/<car_id>',
                 methods=['GET', 'POST', 'PUT', 'DELETE'])

api.add_resource(CarList, '/cars',
                 methods=['GET'])