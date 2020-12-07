import logging


def configure_logger():
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    format = logging.Formatter('%(asctime)s - %(message)s', datefmt='%H:%M:%S')
    handler.setFormatter(format)
    logger.addHandler(handler)
    logger.setLevel(level=logging.INFO)
