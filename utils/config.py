import logging
import logging.handlers

__all__ = (
    'config',
    'enum'
    'LOG_DEBUG',
    'LOG_INFO',
    'LOG_WARN',
    'LOG_ERROR',
    'LOG_CRIT',
)

config = {
    'LOG': {
        'LEVEL': logging.DEBUG,
        'FILE': './log/app.log',
        'MAX_BYTES': 100*1024*1024,
        'BACKUP_COUNT': 3,
        'FORMAT': '[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] [%(module)s:%(funcName)s] %(message)s',
    },
}

logger = logging.getLogger('app_name')
logger.setLevel(logging.DEBUG)
fh = logging.handlers.RotatingFileHandler(filename=config['LOG']['FILE'], maxBytes=config['LOG']['MAX_BYTES'],
                                          backupCount=config['LOG']['BACKUP_COUNT'])
fh.setLevel(config['LOG']['LEVEL'])
formatter = logging.Formatter(config['LOG']['FORMAT'])
fh.setFormatter(formatter)
logger.addHandler(fh)

LOG_DEBUG = logger.debug
LOG_INFO = logger.info
LOG_WARN = logger.warning
LOG_ERROR = logger.error
LOG_CRIT = logger.critical

enum = {
}
