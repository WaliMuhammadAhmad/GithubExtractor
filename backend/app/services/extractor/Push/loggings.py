import logging
import os

def loggers(logging_path='logs/logger.log'):
    """
    This function is used almost everywhere, where the logging is required. 
    Returns a logger instance that writes to the specified log file.

    Args:
        logging_path (str): The path where the log file will be created. By default it will created at `logs/logger.log`.

    Returns:
        logger (logger instance): Configured logger instance with custom instruct.
    """
    
    os.makedirs(os.path.dirname(logging_path), exist_ok=True)
    
    logger = logging.getLogger(logging_path)
    logger.setLevel(logging.INFO)  # Set the default logging level to [INFO]

    file_handler = logging.FileHandler(logging_path)
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(formatter)

    if not logger.handlers:  # Avoid adding handlers multiple times in the same session
        logger.addHandler(file_handler)

    return logger