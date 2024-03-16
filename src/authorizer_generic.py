import logging
import requests
from src.decorators import log_class_and_method
from src.exceptions import InvalidTokenError, InvalidTokenAlg, JwksUriNotFound, JwksEmptyKeys, KidNotFound


class AuthorizerGeneric:
    def __init__(self, token, d_token, h_token):
        self.token = token
        self.d_token = d_token
        self.h_token = h_token

    @log_class_and_method("Iniciando validação do token")
    def authorize(self):
        raise NotImplementedError()

    @log_class_and_method("Validando algoritmo do token")
    def check_alg(self):
        alg = self.h_token.get('alg')
        allow_alg = ["HS256", "RS256"]
        if alg in allow_alg:
            return alg
        raise InvalidTokenAlg(f"Algoritmo {alg} invalido")

    @log_class_and_method("Iniciando chamada ao well-known")
    def request_well_known(self, url):
        well_known_url = f"{url}/.well-known/openid-configuration"
        response = requests.get(well_known_url)
        response.raise_for_status()

        jwks_uri = response.json().get('jwks_uri')
        if not jwks_uri:
            raise JwksUriNotFound("Falha ao obter valor do endpoint jwks")
        return jwks_uri

    @log_class_and_method("Iniciando chamada para obter jwks")
    def request_jwk(self, url):
        response = requests.get(url)
        response.raise_for_status()

        jwks = response.json().get('keys')
        if not jwks:
            raise JwksEmptyKeys("Chaves de jwks vazias")

        for jwk_key in jwks:
            if jwk_key.get('kid') == self.h_token.get("kid"):
                return jwk_key
        raise KidNotFound("Kid não foi enncontrado dentro das chaves jwks")

    @log_class_and_method("Validando assinatura do token")
    def check_signature(self, public_key):
        try:
            rsa_key = jwt.algorithms.RSAAlgorithm.from_jwk(public_key)
            jwt.decode(self.token, key=rsa_key, algorithms=['RS256'])
            return True
        except Exception as e:
            raise InvalidTokenError("Token invalido")

    @log_class_and_method("Obtendo scopes do token")
    def get_scopes(self):
        scopes = self.d_token.get('scope')
        if scopes is not None:
            return scopes.split(" ")
        return None
