#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
from api.v1.auth.auth import Auth
import os


app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


auth = None
if os.getenv('AUTH_TYPE') == 'auth':
    auth = BasicAuth()

else:
    auth = Auth()


@app.before_request
def before_request_func():
    """
    checks if the request path requires authentication and,
    aborts the request with the appropriate status code if necessary.
    """

    # If auth is None, do nothing and proceed with the request
    if auth is None:
        return

    # List of paths that do not require authentication
    excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/',
                      '/api/v1/forbidden/']

    # If the request path does not require authentication,
    # do nothing and proceed with the request
    if not auth.require_auth(request.path, excluded_paths):
        return

    # If the request does not have an Authorization header,
    # abort the request with a 401 Unauthorized status
    if auth.authorization_header(request) is None:
        abort(401)

    # If there is no current user,
    # abort the request with a 403 Forbidden status
    if auth.current_user(request) is None:
        abort(403)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Unauthorized
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
