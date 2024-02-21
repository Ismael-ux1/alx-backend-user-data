#!/usr/bin/env python3
""" Hash Password """
import bcrypt


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
