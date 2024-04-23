import logging

class Logger:
    def __init__(self,logger):
        self.logger = logging.getLogger(logger)

    def get_log(self):
        return self.logger



