#!/usr/bin/env python3
""" Session authentication """
from api.v1.auth.auth import Auth
import uuid
import os
from flask import request
from models.user import User


class SessionAuth(Auth):
    """ session class that inherits from Auth """

    # Initialize a class attribute as an empty dictionary to,
    # store session IDs and user ID's
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Define a method to create a session """

        # If the user_id is None or not is a string, return None
        if user_id is None or type(user_id) != str:
            return None
        else:
            # Generate a unique session ID
            session_id = str(uuid.uuid4())

            # Store the session ID and user ID in the dictionary
            self.user_id_by_session_id[session_id] = user_id

            # Return the session ID
            return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Return a User ID based on a session ID. """

        # If the session_id is None or not a string, return None
        if session_id is None or type(session_id) != str:
            return None
        else:
            # If there is no user associated with the session ID
            # .get() will return None
            return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        Returns a User instance based on a cookie value
        """
        # Get the session ID from the cookie
        session_id = self.session_cookie(request)

        # Get the user ID associated with the session ID
        user_id = self.user_id_for_session_id(session_id)

        # Return the User instance associated with the user ID
        return User.get(user_id)

    def destroy_session(self, request=None):
        """
        Deletes the user session / logout.
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False

        del self.user_id_by_session_id[session_id]
        return True
