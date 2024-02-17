#!/usr/bin/env python3
""" Basic auth """
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth that inherits from auth """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Method that returns the Base64 part of the Authorization header
        for Basic Authentication.

        Parameters:
        authorization_header (str): The Authorization header value.

        Returns:
        str: The Base64 part of the Authorization header if it exists,
             None otherwise.
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith('Basic '):
            return None

        return authorization_header[6:]
