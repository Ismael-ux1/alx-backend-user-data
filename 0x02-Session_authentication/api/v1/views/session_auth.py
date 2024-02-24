#!/usr/bin/env python3
""" Flask view for session_auth. """
from flask import Flask, request, jsonify, make_response
from api.v1.views import app_views
from models.user import User
from api.v1.app import auth
import os

@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """
    Handles user login process by validating email and password,
    and creating a session.
    """
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400

    users = User.search({'email': email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    for user in users:
        if user.is_valid_password(password):
            session_id = auth.create_session(user.id)
            response = make_response(user.to_json())
            response.set_cookie(os.getenv('SESSION_NAME'), session_id)
            return response

    return jsonify({"error": "wrong password"}), 401
