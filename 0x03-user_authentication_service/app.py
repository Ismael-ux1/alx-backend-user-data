#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask, jsonify

# Create an instance of the Flask class
app = Flask(__name__)


@app.route("/")
def hello():
    """ Define a route for the GET method """
    # Return a JSON payload with a message
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    """ Run the app if this module is executed """
    app.run(host="0.0.0.0", port="5000")
