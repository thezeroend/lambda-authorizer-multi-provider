from src.authorizer_generic import AuthorizerGeneric

class Provider2Authorizer(AuthorizerGeneric):
    def authorize(self):
        return False
