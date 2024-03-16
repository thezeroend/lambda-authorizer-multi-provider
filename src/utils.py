def extract_bearer_token(authorization):
    if authorization.startswith('Bearer '):
        return authorization[len('Bearer '):]
    return None
