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
        bool: True if the path is not in the list of strings excluded_paths,
              False otherwise.
        """
        if path is None:
            return True

        if not excluded_paths:
            return True

        # Ensure path ends with a '/'
        if not path.endswith('/'):
            path += '/'

        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """
        Method that returns the value of the Authorization header,
        from the request.

        Parameters:
        request: The Flask request object.

        Returns:
        str: The value of the Authorization header if it exists,
        None otherwise
        """
        if request is None:
            return None

        return request.headers.get('Authorization', None)

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
