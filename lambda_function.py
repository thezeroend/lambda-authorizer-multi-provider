import logging
import os
from src.authorizer_factory import AuthorizerFactory
from src.authorizer_generic import AuthorizerGeneric
from src.policy_generator import generate_policy
from src.utils import extract_bearer_token
from src.exceptions import HeaderMissing


def set_log_level():
    log_level = os.environ.get('LOG_LEVEL', 'INFO').upper()
    numeric_level = getattr(logging, log_level, None)
    if not isinstance(numeric_level, int):
        raise ValueError(f'Invalid log level: {log_level}')
    logging.basicConfig(level=numeric_level)

set_log_level()
authorizer_factory = AuthorizerFactory()

class VerifyAuth:
    def __init__(self, event, context):
        self.event = event
        self.headers = {key.lower(): value for key, value in event.get('headers', {}).items()}
        self.context = context

    def verify(self):
        if self.headers.get("authorization") is None:
            raise HeaderMissing("Header Authorization ausente")
        token = extract_bearer_token(self.headers.get("authorization"))

        if not token:
            return generate_policy('user', 'Deny', event['methodArn'])

        try:
            authorizer = authorizer_factory.create_authorizer(token)
            authorizer.authorize()
        except Exception as e:
            logging.error("Erro personalizado:", e)

        return generate_policy("*", 'Allow', "*")


def lambda_handler(event, context):
    return VerifyAuth(event, context).verify()