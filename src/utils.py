import os
import logging
from src.exceptions import InvalidTokenError

def extract_bearer_token(authorization):
    if authorization.startswith('Bearer '):
        return authorization.split(" ")[1]
    return authorization

def set_log_level():
    log_level = os.environ.get('LOG_LEVEL', 'INFO').upper()
    numeric_level = getattr(logging, log_level, None)
    if not isinstance(numeric_level, int):
        raise ValueError(f'Invalid log level: {log_level}')
    logging.basicConfig(level=numeric_level)