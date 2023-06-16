import logging, sys

__name__ = "data_cleansing"
FORMAT = '%(asctime)s %(name)s %(levelname)s %(message)s '

h1 = logging.StreamHandler(sys.stdout)
f = logging.Formatter(FORMAT, datefmt="%Y-%m-%d %H:%M:%S")
h1.setFormatter(f)
logger = logging.getLogger("my.logger")
logger.addHandler(h1)
logger.setLevel(logging.DEBUG)
logger.debug("A DEBUG message")
logger.info("An INFO message")
logger.warning("A WARNING message")
logger.error("An ERROR message")
logger.critical("A CRITICAL message")