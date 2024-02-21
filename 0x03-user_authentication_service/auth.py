#!/usr/bin/env python3
""" Hash Password """
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


class Auth:
    """Auth class to interact with the authentication database.
    """
    def __init__(self):
        """ initialize """
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        """Hash a password using bcrypt
        Args:
        password (str): The password to hash

        Returns:
        bytes: The hashed password
        """
        # Generate a random salt
        salt = bcrypt.gensalt()

        # Hash the password with the salt
        hashed_password = bcrypt.hashpw(password.encode(), salt)
        return hashed_password

    def register_user(self, email: str, password: str) -> User:
        """Register a new user

        Args:
            email (str): The email of the user
            password (str): The password of the user

        Returns:
            User: The created User object

        Raises:
            ValueError: If a user already exists with the given email
        """
        # Check if a user already exists with the given email
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            pass

        # Hash the password
        hashed_password = self._hash_password(password)

        # Save the user to the database and return the User object
        user = self._db.add_user(email=email, hashed_password=hashed_password)

        return user