from flask_restful import Api
from src.resources.pokemon import ComparePokemon


def configure_routes(app):
    api = Api(app)
    api.add_resource(ComparePokemon, '/compare')
