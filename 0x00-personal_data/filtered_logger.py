#!/usr/bin/env python3
""" A function that returns the log message obfuscated """
import re


def filter_datum(fields: list, redaction: str, message: str,
                 separator: str) -> str:
    pattern = '|'.join(f'{field}=[^;]*' for field in fields)
    return re.sub(pattern,
                  lambda m: m.group().replace(
                      m.group().split('=')[1], redaction),
                  message)
