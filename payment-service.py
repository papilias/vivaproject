# payment-service.py

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import requests

app = Flask(__name__)
api = Api(app)

class Payment(Resource):
    def post(self):
        data = request.get_json()
        order_data = requests.get('http://localhost:5001/order/' + data['order_id']).json()
        # Perform payment processing logic using order_data
        return jsonify({'message': 'Payment processed successfully'})

api.add_resource(Payment, '/payment')

if __name__ == '__main__':
    app.run(port=5002)