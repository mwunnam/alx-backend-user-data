#!/usr/bin/env python3
"""Authentication Part"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    This hashes a passowrd by using bcrypt
    Args:
        password (str): the sting to be harsed
    Return:
        bytes
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed
