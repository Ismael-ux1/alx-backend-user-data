#!/usr/bin/env python3
""" Hash a password using bcrypt. """
import bcrypt


def hash_password(password: str) -> bytes:
    """ Hash a password using bcrypt. """
    # convert the password to bytes
    password_bytes = password.encode('utf-8')

    # Generate a salt
    salt = bcrypt.gensalt()

    # Hash the password
    hashed_password = bcrypt.hashpw(password_bytes, salt)

    return hashed_password
