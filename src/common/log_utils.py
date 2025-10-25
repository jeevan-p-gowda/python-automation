# Module-level logger that will be set by conftest
import functools
import logging
import os

_logger = None


def set_logger(args: str):
    """Set the logger instance to be used elsewhere."""
    log_obj = logging.getLogger()
    log_obj.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] (%(filename)s:%(lineno)d) %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    log_obj.addHandler(console_handler)
    if "/ui" in args:
        log_dir = "results/ui"
        os.makedirs(log_dir, exist_ok=True)
        file_handler = logging.FileHandler(f"{log_dir}/ui.log", mode="w")
        file_handler.setFormatter(formatter)
        log_obj.addHandler(file_handler)
    elif "/api" in args:
        log_dir = "results/api"
        os.makedirs(log_dir, exist_ok=True)
        file_handler = logging.FileHandler(f"{log_dir}/api.log", mode="w")
        file_handler.setFormatter(formatter)
        log_obj.addHandler(file_handler)
    else:
        raise ValueError(f"Invalid test path: {args}. Expected /ui or /api in path.")
    global _logger
    _logger = log_obj
    return log_obj


def logger():
    """Get the current logger instance."""
    if _logger is None:
        raise RuntimeError(
            "Logger not initialized. Make sure tests are run through pytest."
        )
    return _logger


def log(func):
    """Decorator to log function name when called."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if _logger:
            _logger.info(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


def pretty_print_request_and_response(response):
    pretty_print_request(response)
    pretty_print_response(response)


def pretty_print_request(response):
    _logger.info(f"Request URL:         {response.request.url}")
    _logger.info(f"Request Method:      {response.request.method}")


def pretty_print_response(response):
    _logger.info(f"Response Code:       {response.status_code}")
    _logger.info(f"Response Time:       {response.elapsed.total_seconds()} seconds")
