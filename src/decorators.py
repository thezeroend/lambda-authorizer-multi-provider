import logging
import functools

def log_class_and_method(log_message="Executando", finish_message="Finalizada"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            class_name = args[0].__class__.__name__  # Obtém o nome da classe da instância
            method_name = func.__name__  # Obtém o nome da função
            
            # Configura o logger com o nome da classe e do método
            # logger = logging.getLogger(f"{class_name}.{method_name}")
            
            # Adiciona o nome da classe e do método ao registro de log
            logging.info("[%s][%s] - %s", class_name, method_name, log_message)
            
            # Chama a função original
            result = func(*args, **kwargs)

            logging.info("[%s][%s] - %s", class_name, method_name, finish_message)
            return result
        return wrapper
    return decorator