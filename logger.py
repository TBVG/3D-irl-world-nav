import logging

def setup_logger(name, level=logging.INFO):
    """
    Sets up a logger with a specific name and logging level.
    Logs will include timestamp, logger name, log level, and the message.
    
    :param name: Name of the logger
    :param level: Logging level (default is INFO)
    :return: Configured logger object
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger

# Example of setting up the logger for the application
app_logger = setup_logger('NavigationApp')
