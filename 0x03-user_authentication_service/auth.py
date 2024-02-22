#!/usr/bin/env python3
""" Hash Password """
import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


def _hash_password(password: str) -> bytes:
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


def _generate_uuid() -> str:
    """Generate a new UUID

    Returns:
        str: The string representation of the new UUID
    """
    # Generate a new UUID
    new_uuid = uuid.uuid4()

    # Return the string representation of the UUID
    return str(new_uuid)


class Auth:
    """Auth class to interact with the authentication database.
    """
    def __init__(self):
        """ initialize """
        self._db = DB()

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
            # Attempt to find a user with the given email
            user = self._db.find_user_by(email=email)
            # If a user is found, raise a ValueError
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            # If no user is found, hash the password
            hashed_password = _hash_password(password)
            # Add the new user to the database and return the User object
            return self._db.add_user(email=email,
                                     hashed_password=hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """Validate login

        Args:
        email (str): The email of the user
        password (str): The password of the user

        Returns:
        bool: True if the password matches, False otherwise
        """
        try:
            # Locate the user by email
            user = self._db.find_user_by(email=email)
            # Check the password
            return bcrypt.checkpw(password.encode(), user.hashed_password)
        except NoResultFound:
            return False
