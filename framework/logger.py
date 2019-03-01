import logging
import os
import time

class Logger(object):
    def __init__(self,logger):
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        log_path=os.path.dirname(os.path.abspath('.'))+'/logs/'
        log_name=log_path+rq+'.log'


        self.fh=logging.FileHandler(log_name)
        self.ch=logging.StreamHandler()
        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)

        self.format=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        self.fh.setFormatter(self.format)
        self.ch.setFormatter(self.format)

        # self.logger.debug("debug日志信息")
        # self.logger.info("info日志信息")
        # self.logger.warning("warning日志信息")
        # self.logger.error("error日志信息")

    def getlog(self):
        return self.logger