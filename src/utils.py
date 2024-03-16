from src.exceptions import InvalidTokenError

def extract_bearer_token(authorization):
    if authorization.startswith('Bearer '):
        return authorization.split(" ")[1]
    return authorization
