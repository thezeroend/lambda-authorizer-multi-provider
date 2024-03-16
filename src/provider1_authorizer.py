import logging
from src.authorizer_generic import AuthorizerGeneric
from src.decorators import log_class_and_method 

class Provider1Authorizer(AuthorizerGeneric):
    @log_class_and_method("Iniciando validação do token")
    def authorize(self):

        alg = self.check_alg()

        if alg == "RS256":
            jwk_url = self.request_well_known("https://auth0.openai.com")
            jwk = self.request_jwk(jwk_url)
            return self.check_signature
        else:
            logging.info("Não implementado ainda")
        return True
