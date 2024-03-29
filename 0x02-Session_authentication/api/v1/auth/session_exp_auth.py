#!/usr/bin/env python3
""" expiration date to a Session ID. """
from api.v1.auth.session_auth import SessionAuth
from models.user import User
from datetime import datetime, timedelta
import os


class SessionExpAuth(SessionAuth):
    """Class that handles session expiration authentication."""
    def __init__(self):
        """Initializes the SessionExpAuth instance."""
        self.session_duration = int(os.getenv('SESSION_DURATION', 0))

    def create_session(self, user_id=None):
        """
        Creates a session ID and stores it with its associated
        user ID and creation time.
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        session_dictionary = {'user_id': user_id,
                              'created_at': datetime.now()}
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Returns a user ID based on a session ID,
        considering the session duration.
        """
        if session_id is None:
            return None
        session_dictionary = self.user_id_by_session_id.get(session_id)
        if session_dictionary is None:
            return None
        user_id = session_dictionary.get('user_id')
        if self.session_duration <= 0:
            return user_id
        if 'created_at' not in session_dictionary:
            return None
        if session_dictionary.get('created_at') + \
                timedelta(seconds=self.session_duration) < datetime.now():
            return None
        return user_id
