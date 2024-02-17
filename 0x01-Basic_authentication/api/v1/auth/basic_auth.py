#!/usr/bin/env python3
""" Basic auth """
import base64
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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """
        Method that returns the decoded value of,
        a Base64 string base64_authorization_header.

        Parameters:
        base64_authorization_header (str):
        The Base64 part of the Authorization header.

        Returns:
        str: The decoded value of base64_authorization_header,
        if it is a valid Base64 string, None otherwise.
        """
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            base64_bytes = base64_authorization_header.encode('utf-8')
            message_bytes = base64.b64decode(base64_bytes)
            return message_bytes.decode('utf-8')
        except Exception:
            return None
