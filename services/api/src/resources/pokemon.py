from flask_restful import Resource
from flask import request


class ComparePokemon(Resource):
    def get(self):
        status_code = 200
        response = ({'message': 'Hello World Pokemon'}, status_code)
        return response
