#!/usr/bin/env python3
"""
main
"""
import requests
from auth import Auth

EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


def register_user(email: str, password: str) -> None:
    """Register a new user."""
    pass


def log_in_wrong_password(email: str, password: str) -> None:
    """Attempt to log in with a wrong password."""
    pass


def log_in(email: str, password: str) -> str:
    """Log in with correct credentials."""
    pass


def profile_unlogged() -> None:
    """Attempt to access profile while unlogged."""
    pass


def profile_logged(session_id: str) -> None:
    """Access profile while logged in."""
    pass


def log_out(session_id: str) -> None:
    """Log out from the session."""
    pass


def reset_password_token(email: str) -> str:
    """Generate a reset password token."""
    pass


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Update the password using a reset token."""
    pass


if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
