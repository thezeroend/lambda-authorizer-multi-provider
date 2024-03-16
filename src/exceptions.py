# exceptions.py

class CustomException(Exception):
    """Classe base para exceções personalizadas."""
    pass

class TokenExpiredError(CustomException):
    """Exceção para token JWT expirado."""
    pass

class InvalidTokenError(CustomException):
    """Exceção para token JWT inválido."""
    pass

class HeaderMissing(CustomException):
    """Exceção para header Authorization ausente."""
    pass

class InvalidTokenAlg(CustomException):
    """Exceção para token com Algoritmo invalido."""
    pass

class JwksUriNotFound(CustomException):
    """Exceção para falha ao obter endpoint do jwks."""
    pass

class JwksEmptyKeys(CustomException):
    """Exceção para falha retorno vazio do endpoint de jwks."""
    pass

class KidNotFound(CustomException):
    """Exceção para falha kid não encontrado nas chaves jwks."""
    pass