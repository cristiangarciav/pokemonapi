from flask_restful import Api
from flask import Flask
from src.resources.pokeresources import ComparePokemon, CommonMoves


def configure_routes(app: Flask) -> None:
    api = Api(app)
    api.add_resource(ComparePokemon, '/compare_damage')
    api.add_resource(CommonMoves, '/common_moves')
