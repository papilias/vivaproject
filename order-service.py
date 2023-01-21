# order-service.py

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import requests

app = Flask(__name__)
api = Api(app)

class Order(Resource):
    def post(self):
        data = request.get_json()
        user_data = requests.get('http://localhost:5000/user/' + data['user_id']).json()
        # Perform order creation logic using user_data
        return jsonify({'message': 'Order created successfully'})
    
    def get(self, order_id):
        #