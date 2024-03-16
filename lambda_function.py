import logging
import os
from src.authorizer_factory import AuthorizerFactory
from src.authorizer_generic import AuthorizerGeneric
from src.policy_generator import generate_policy
from src.utils import extract_bearer_token, set_log_level, setup_env
from src.exceptions import HeaderMissing
from src.decorators import log_class_and_method
from src.permissions import Permissions


setup_env()
set_log_level()
authorizer_factory = AuthorizerFactory()
permissions = Permissions()

class VerifyAuth:
    def __init__(self, event, context):
        self.event = event
        self.context = context
        self.headers = {key.lower(): value for key, value in event.get('headers', {}).items()}

    @log_class_and_method("Iniciando verificação")
    def verify(self):
        if self.headers.get("authorization") is None:
            raise HeaderMissing("Header Authorization ausente")
        token = extract_bearer_token(self.headers.get("authorization"))

        if not token:
            return generate_policy('user', 'Deny', self.event['methodArn'])

        try:
            authorizer = authorizer_factory.create_authorizer(token)
            authorizer.authorize()
            
            if not permissions.validate_scopes(authorizer.get_scopes(), self.event["resource"], self.event["httpMethod"]):
                return generate_policy('user', 'Deny', self.event['methodArn'])
        except Exception as e:
            logging.error("Erro personalizado:", e)

        return generate_policy("*", 'Allow', "*")


def lambda_handler(event, context):
    return VerifyAuth(event, context).verify()