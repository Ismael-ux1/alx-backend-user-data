#!/usr/bin/env python3
""" A function that returns the log message obfuscated """
import re


def filter_datum(fields: [list], redaction: str, message: str, separator: str) -> str:
    # Compile regex pattern to avoid recompilation in each iteration
    pattern = re.compile('|'.join(f'{re.escape(field)}=[^{re.escape(separator)}]*' for field in fields))
    
    # Use a lambda function to perform the substitution with the redaction string
    return pattern.sub(lambda match: f'{match.group().split("=")[0]}={redaction}', message)
