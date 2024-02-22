#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask, jsonify, request, make_response, abort, redirect
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


@app.route('/sessions', methods=['POST'])
def login() -> str:
    """ function to respond to the POST /sessions route. """
    email = request.form.get('email')
    password = request.form.get('password')

    # Validate the email and password
    if not AUTH.valid_login(email, password):
        abort(401)

    # If the login information is correct, create a new session for the user
    session_id = AUTH.create_session(email)

    # Create a response with a JSON payload
    response = make_response(jsonify({"email": "<user email>",
                             "message": "logged in"}), 200)

    # Store the session ID as a cookie with key "session_id" on the response
    response.set_cookie('session_id', session_id)

    return response


@app.route('/sessions', methods=['DELETE'])
def logout() -> str:
    """ function to respond to the DELETE /sessions route. """
    # Get the session ID from the cookies
    session_id = request.cookies.get('session_id')

    # Find the user with the requested session ID
    user = AUTH.get_user_from_session_id(session_id)

    # If the user exists
    if user:
        # Destroy the session
        AUTH.destroy_session(user.id)
        # Redirect the user to GET /
        return redirect('/')
    else:
        # If the user does not exist, respond with a 403 HTTP status
        abort(403)


def profile() -> str:
    """ function that respond to the GET /profile route. """
    # Get the session ID from the cookies
    session_id = request.cookies.get('session_id')

    # Find the user with the requested session ID
    user = AUTH.get_user_from_session_id(session_id)

    # If the user exists
    if user:
        # Respond with a 200 HTTP status and the user's email
        return jsonify({"email": user.email}), 200
    else:
        # If the user does not exist, respond with a 403 HTTP status
        abort(403)


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token() -> str:
    """ function that respond to the POST /reset_password route. """
    # Get the email from the form data
    email = request.form.get('email')

    # Try to find the user with the given email
    try:
        user = AUTH.get_user_by(email=email)
    except ValueError:
        # If the email is not registered, respond with a 403 status code
        abort(403)

    # If the user exists, generate a token
    reset_token = AUTH.get_reset_password_token(email)

    # Respond with a 200 HTTP status and the email and reset token
    return jsonify({"email": email, "reset_token": reset_token}), 200


if __name__ == "__main__":
    """ Run the app if this module is executed """
    app.run(host="0.0.0.0", port="5000")
