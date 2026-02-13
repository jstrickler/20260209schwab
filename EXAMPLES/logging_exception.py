import logging

logging.basicConfig( # configure logging
    filename='../LOGS/exception.log',
    format='%(levelname)s %(name)s %(asctime)s %(filename)s %(module)s %(funcName)s %(lineno)d %(message)s', # set the format for log entries
    datefmt="%x-%X",

    level=logging.WARNING,  # minimum level
)

for i in range(3):
    try:
        result = i/0
    except ZeroDivisionError:
        logging.exception('Logging with exception info') # add exception info to the log
