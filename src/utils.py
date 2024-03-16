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

def setup_env():
    ENVS_DEFAULT = {
        "dev": {
            "LOG_LEVEL": "debug",
            "PROVIDER1_HOST": "https://auth0.openai.com",
            "PROVIDER1_ISS": "https://auth0.openai.com/",
            "PROVIDER2_HOST": "https://provider2.com",
            "PROVIDER2_ISS": "https://provider2.com/",
        },
        "hom": {
            "LOG_LEVEL": "debug"
        },
        "prod": {
            "LOG_LEVEL": "info"
        }
    }

    if os.environ.get('ENV') is None:
        os.environ['ENV'] = os.environ.get('var1')
    env = os.environ.get('ENV')

    for key in ENVS_DEFAULT[env]:
        if os.environ.get(key) is None:
            os.environ[key] = ENVS_DEFAULT[env][key]