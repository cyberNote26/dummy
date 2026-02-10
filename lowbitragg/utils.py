import logging
import time

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def count_tokens(text):
    """Counts the number of tokens in a given text."""
    return len(text.split())


def log_performance(func):
    """Decorator to log performance metrics of functions."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(f'Execution time for {func.__name__}: {end_time - start_time:.4f} seconds')
        return result
    return wrapper


def validate_data(data, expected_type):
    """Validates that data is of the expected type."""
    if not isinstance(data, expected_type):
        raise ValueError(f'Expected data of type {expected_type}, but got {type(data)}')

    return True
