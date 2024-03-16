import logging
import functools

def log_class_and_method(log_message="Executando", finish_message="Finalizada"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            class_name = args[0].__class__.__name__ 
            method_name = func.__name__
            logging.info("[%s][%s] - %s", class_name, method_name, log_message)
            result = func(*args, **kwargs)
            logging.info("[%s][%s] - %s", class_name, method_name, finish_message)
            return result
        return wrapper
    return decorator