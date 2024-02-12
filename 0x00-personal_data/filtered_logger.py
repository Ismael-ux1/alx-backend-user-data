#!/usr/bin/env python3
""" A function that returns the log message obfuscated """
import re
import logging
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ A function that returns the log message obfuscated """
    for field in fields:
        pattern = f"{field}=[^{separator}]*"
        message = re.sub(pattern, f"{field}={redaction}", message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Constructor for the RedactingFormatter class. """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Format the specified record as text. """
        original_message = super().format(record)
        return filter_datum(self.fields,
                            self.REDACTION, original_message, self.SEPARATOR)
