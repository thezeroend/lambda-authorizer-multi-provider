from src.authorizer_generic import AuthorizerGeneric

class Provider2Authorizer(AuthorizerGeneric):
    def authorize(self):
        # Implemente a lógica de autorização específica para o provider 2
        # Use self.token_info para acessar as informações do token, se necessário
        # Retorna True se o acesso for permitido e False caso contrário
        return False  # Exemplo: nunca permitir acesso para demonstração
