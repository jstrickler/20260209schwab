import logging
import sys
import os

match sys.platform:
    case 'win32':
        log_folder = os.getenv('SYSTEMDIR')
    case 'darwin':
        log_folder = '/var/logs'
    case 'linux':
        log_folder = '/var/logs'

logging.basicConfig(
    format='%(levelname)s %(name)s %(asctime)s %(filename)s %(module)s %(funcName)s %(lineno)d %(message)s', # set the format for log entries
    datefmt="%x-%X",
    filename='../LOGS/formatted.log',
    level=logging.INFO,
)

def main():
    logging.info("this is information")
    logging.warning("this is a warning")
    logging.error("this is an ERROR")
    value = 38.7
    logging.error("Invalid value %s", value)
    logging.info("this is information")
    logging.critical("this is critical")

if __name__ == "__main__":
    main()



