import logging
logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG, filename = 'log.txt', datefmt = '%d-%m-%Y %H:%M:%S',) # '%(asctime)s %(levelname)s:%(message)s',
# logger = logging.getLogger('test_logger')
logger = logging.getLogger('books')
logger.info('This is info message!')
logger.warning('This is warning message!!')

"""
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""