import logging.config


logging.basicConfig(
    filename='log.log',
    level=logging.NOTSET,
    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s'
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.NOTSET)
logger_handler = logging.StreamHandler()
logger.addHandler(logger_handler)
