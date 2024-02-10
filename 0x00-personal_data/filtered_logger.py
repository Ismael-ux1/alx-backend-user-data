#!/usr/bin/env python3
""" A function that returns the log message obfuscated """
import re


def filter_datum(fields: list, redaction: str, message: str,
                 separator: str) -> str:
    """ A function that returns the log message obfuscated """
    for field in fields:
        message = re.sub(f"{field}=[^;]*", f"{field}={redaction}", message)
    return message
