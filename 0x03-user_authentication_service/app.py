#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask, jsonify, request, make_response
from auth import Auth

# Create an instance of the Flask class
app = Flask(__name__)
AUTH = Auth()


@app.route("/")
def hello():
    """ Define a route for the GET method """
    # Return a JSON payload with a message
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """ function that implements the POST /users route """
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    """ Run the app if this module is executed """
    app.run(host="0.0.0.0", port="5000")
