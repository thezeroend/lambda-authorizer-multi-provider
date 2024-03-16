import logging
import functools
import time

def log_class_and_method(log_message="Executando", finish_message="Finalizado"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            class_name = args[0].__class__.__name__ 
            method_name = func.__name__
            start_time = time.time()
            logging.info("[%s][%s] - %s", class_name, method_name, log_message)
            result = func(*args, **kwargs)
            end_time = time.time()
            duration = (end_time - start_time) * 1000
            duration = "{:.3f}".format(duration)
            logging.info("[%s][%s] - %s - %s ms", class_name, method_name, finish_message, duration)
            return result
        return wrapper
    return decorator