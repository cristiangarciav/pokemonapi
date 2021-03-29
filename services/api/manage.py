from flask.cli import FlaskGroup
from src.app import app

# Binding the app instance to the Command line interface:
cli = FlaskGroup(app)

if __name__ == '__main__':
    cli()
