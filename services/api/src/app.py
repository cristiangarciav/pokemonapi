from flask import Flask
from src.handlers.routes import configure_routes

# Instantiating the main Flask application

app = Flask(__name__)
# The secret key should be stored in a secure place.
# For timing issues this is going to be changed in future deployments
app.secret = "my-super-secret-very-long-key"

# Function that configures the end-points
configure_routes(app)
