#!/usr/bin/env python3
""" API Authentication """
from flask import request
from typing import List, TypeVar

User = TypeVar('User')


class Auth():
    """ Class that manage the API authentication """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:

        """
        Method that checks if a particular path requires authentication.

        Argumetns:
        path (str): The path to check.
        excluded_paths (List[str]): The List of paths that,
                                    don't require authentication.


        Returns:
        bool:
        """
        # Path and excluded_paths will be used later
        return False

    def authorization_header(self, request=None) -> str:
        """
        Method that returns the value of the Authorization header,
        from the request.

        Parameters:
        request: The Flask request object.

        Returns:
        str: None for now, will be updated in the future.
        """
        # request will be the flask request object
        return None

    def current_user(self, request=None) -> User:
        """
        Method that returns the current user based on the request.

        Parameters:
        request: The Flask request object.

        Returns:
        User: None for now, will be updated in the future.
        """
        # request will be the flask request object
        return None
