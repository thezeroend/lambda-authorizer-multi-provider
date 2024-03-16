import json
import logging
from src.decorators import log_class_and_method


class Permissions:
    def __init__(self):
        self.permissions = self.load_permissions("./src/files/permissions.json")
    
    @log_class_and_method("Carregando arquivo de permissions")
    def load_permissions(self, file_path):
        with open(file_path, "r") as file:
            return json.load(file)

    @log_class_and_method("Verificando permissão nos scopes")
    def validate_scopes(self, scopes, route, method):
        for permission in self.permissions:
            if permission["rota"] == route and method in permission["methods"]:
                required_scopes = permission["scopes"]
                if all(scope in scopes for scope in required_scopes):
                    return True
        return False