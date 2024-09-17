#!/usr/bin/env python3
''' log message obfuscating '''
import re


def filter_datum(fields, redaction, message, separator):
    """Function returns Obfuscated log message"""
    for field in fields:
        message = re.sub(f'{field}=[^{separator}]*', f'{field}={redaction}', message)
    return message
