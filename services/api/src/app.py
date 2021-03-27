from flask import Flask
from src.handlers.routes import configure_routes

app = Flask(__name__)
app.secret = "my-super-secret-very-long-key"
configure_routes(app)
