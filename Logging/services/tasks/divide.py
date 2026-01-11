import logging

logger = logging.getLogger(__name__)

def run():
    logger.info("Divide task started !")
    result = 10 / 0
    return result
