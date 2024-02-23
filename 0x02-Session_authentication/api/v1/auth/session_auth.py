#!/usr/bin/env python3
""" Session authentication """
from api.v1.auth.auth import Auth
import uuid


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
