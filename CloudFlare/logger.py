from __future__ import (absolute_import, unicode_literals,
                        division, print_function)

import logging

DEBUG = 0
INFO = 1


class Logger(object):
    def __init__(self, level):
        self.logger_level = self._get_logging_level(level)

	def getLogger(self):
		# create logger
		logger = logging.getLogger('Python CloudFlare API v4')
		logger.setLevel(self.logger_level)

		ch = logging.StreamHandler()
		ch.setLevel(self.logger_level)

		# create formatter
		formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

		# add formatter to ch
		ch.setFormatter(formatter)

        # create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

		return logger

        # add ch to logger
        logger.addHandler(ch)

        return logger

    def _get_logging_level(self, level):
        if level is True:
            return logging.DEBUG
        else:
            return logging.INFO
