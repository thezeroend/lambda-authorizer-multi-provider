import jwt
import logging
import traceback
from src.provider1_authorizer import Provider1Authorizer
from src.provider2_authorizer import Provider2Authorizer
from src.exceptions import InvalidTokenError, TokenExpiredError
from src.decorators import log_class_and_method

class AuthorizerFactory:
    def __init__(self):
        self.providers = {
            'https://auth0.openai.com/': Provider1Authorizer,
            'authorizer2.com': Provider2Authorizer
        }

    @log_class_and_method("Iniciando criação do Authorizer")
    def create_authorizer(self, token):
        try:
            options = {
                'verify_signature': False,  # Não validar a assinatura
                'verify_exp': True,         # Verificar se o token está expirado
                'verify_iat': False,        # Não verificar a data de emissão do token
                'verify_aud': False,        # Não verificar a audiência do token
                'verify_iss': False,        # Não verificar o emissor do token
                'require_exp': True,       # Não exigir uma data de expiração no token
            }
            decoded_token = jwt.decode(token, options=options)
            provider = decoded_token.get('iss')
            authorizer_class = self.providers.get(provider)
            if not authorizer_class:
                raise InvalidTokenError("[AuthorizerFactory][Auth002] - Issuer do token não permitido")
            headers_token = jwt.get_unverified_header(token)
            return authorizer_class(token, decoded_token, headers_token)
        except Exception as e:
            logging.error("Traceback:")
            logging.error(e.traceback)
            raise InvalidTokenError(e)