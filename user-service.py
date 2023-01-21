# user-service.py

from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class User(Resource):
    def post(self):
        data = request.get_json()
        # Perform user registration logic
        return jsonify({'message': 'User created successfully'})
    
    def get(self, user_id):
        # Perform user retrieval logic
        return jsonify({'user_id': user_id, 'name': 'John Doe', 'email': 'johndoe@example.com'})

api.add_resource(User, '/user/<int:user_id>')

if __name__ == '__main__':
    app.run(port=5000)