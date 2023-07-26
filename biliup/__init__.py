import logging
import sys

__version__ = "0.4.24"

LOG_CONF = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': "%(asctime)s %(filename)s[line:%(lineno)d](Pid:%(process)d "
                      "Tname:%(threadName)s) %(levelname)s %(message)s",
            # 'datefmt': "%Y-%m-%d %H:%M:%S"
        },
        'simple': {
            'format': '%(filename)s%(lineno)d[%(levelname)s]Tname:%(threadName)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': logging.DEBUG,
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'simple'
        },
        'file': {
            'level': logging.DEBUG,
            'class': 'biliup.common.log.SafeRotatingFileHandler',
            'when': 'W0',
            'interval': 1,
            'backupCount': 1,
            'filename': 'ds_update.log',
            'formatter': 'verbose'
        }
    },
    'root': {
        'handlers': ['console'],
        'level': logging.INFO,
    },
    'loggers': {
        'biliup': {
            'handlers': ['file'],
            'level': logging.INFO,
        },
    }
}
