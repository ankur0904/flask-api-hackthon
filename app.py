from flask import Flask, jsonify, request
from functools import wraps
from flask_restful import Api, Resource
from data import data
from my_token import my_token

app = Flask(__name__)
api = Api(app)

def authorize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get('token')
        if not token:
            return {'msg': 'Token not present 🫣'}, 401      
        if token not in my_token:
            return {'msg': 'Invalid Token 😮‍💨'}, 401  
        return func(*args, **kwargs)
    return wrapper

class Hello(Resource):
    @authorize
    def get(self):
        return jsonify({'msg': 'Hello, world'})

    def post(self):
        return jsonify({'msg': 'hello POST'})

class Data(Resource):
    @authorize
    def get(self):
        return jsonify(data)

api.add_resource(Hello, '/')
api.add_resource(Data, '/data')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)