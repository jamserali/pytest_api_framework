import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def setup_logger(name="api_tests", log_file="api_tests.log", level=logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)
    file_formatter = logging.Formatter("%(asctime)s - %(levelname) - %(message)s")
    file_handler.setFormatter(file_formatter)

    # console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter("%(levelname)s: %(message)s")
    console_handler.setFormatter(console_formatter)

    # Add handler to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger


# Initialize a global logger
# logger = setup_logger()
