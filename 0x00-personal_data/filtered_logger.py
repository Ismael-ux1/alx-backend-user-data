#!/usr/bin/env python3
""" A function that returns the log message obfuscated """
import re


def filter_datum(fields: list, redaction: str, message: str,
                 separator: str) -> str:
    """ A function that returns the log message obfuscated """

    # Create a regex pattern for each field to be obfuscated
    pattern = '|'.join(f'{field}=[^;]*' for field in fields)

    # Replace all occurrences of the fields in the message,
    # with the redaction string
    return re.sub(pattern,
                  lambda m: m.group().replace(
                      m.group().split('=')[1], redaction),
                  message)
