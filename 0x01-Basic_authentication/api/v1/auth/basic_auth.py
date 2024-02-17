#!/usr/bin/env python3
""" Basic auth """
import base64
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar


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

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):

        """
        Method that returns the user email and password from,
        the Base64 decoded value.

        Parameters:
        decoded_base64_authorization_header (str):
        The Base64 decoded Authorization header.

        Returns:
        (str, str): The user email and password if they exist,
                    (None, None) otherwise.
        """
        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        credentials = decoded_base64_authorization_header.split(':', 1)
        return credentials[0], credentials[1]

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> User:
        """
        Method that returns the User instance based on his email and password.

        Parameters:
        user_email (str): The email of the user.
        user_pwd (str): The password of the user.

        Returns:
        User: The User instance if it exists and the password is correct,
              None otherwise.
        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        users = User.search({'email': user_email})
        if not users:
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user

            return None

    def current_user(self, request=None) -> User:
        """
        Method that retrieves the User instance for a request.
        Parameters:
        request: The Flask request object.

        Returns:
        User: The User instance if it exists and the password is correct,
              None otherwise.
        """
        authorization_header = \
        self.authorization_header(request)

        base64_authorization_header = \
        self.extract_base64_authorization_header(authorization_header)

        decoded_base64_authorization_header = \
        self.decode_base64_authorization_header(base64_authorization_header)

        user_email, user_pwd = \
        self.extract_user_credentials(decoded_base64_authorization_header)

        return self.user_object_from_credentials(user_email, user_pwd)
