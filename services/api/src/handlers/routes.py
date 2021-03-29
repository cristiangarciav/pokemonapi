from flask_restful import Api
from flask import Flask, render_template
from src.resources.pokeresources import ComparePokemon, CommonMoves


# Function that configures the end-points


def configure_routes(app: Flask) -> None:
    ''' Sets the end-points for the Flask application'''
    api = Api(app)
    api.add_resource(ComparePokemon, '/compare_damage')
    api.add_resource(CommonMoves, '/common_moves')

    @app.route("/")
    def index():
        return render_template("index.html")
