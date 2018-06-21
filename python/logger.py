# -*- coding: utf-8 -*-
#!/usr/bin/env python2.7  
# @Author: Micah20150725
# @Date:   2018-06-19 18:31:59
# @Last Modified by:   Micah20150725
# @Last Modified time: 2018-06-21 16:32:03

# https://www.cnblogs.com/yyds/p/6901864.html
# https://docs.python.org/2/library/logging.handlers.html

# 按文件大小 分割LOG文件
# log_mgr.error(msg) 会将日志存入 fail和log两个之中
# log_mgr.info(msg)  会将日志存入 success和log两个之中
# maxBytes为 success.log fail.log文件的最大值, log文件最大值为maxBytes*2
# backupCount为备份的文件个数

import logging, logging.handlers  
class LogMgr:  
    def __init__ (self, logPath='./log', maxBytes=10*1024, backupCount=50):  
        # log both success & fail log
        self.LOG = logging.getLogger('log')
        loghdlr = logging.handlers.RotatingFileHandler(filename=logPath+'/log', 
                                                        mode="a", maxBytes=maxBytes*2, backupCount=backupCount*2)  
        fmt = logging.Formatter("%(asctime)s %(message)s", "%Y-%m-%d %H:%M:%S")  
        loghdlr.setFormatter(fmt)  
        self.LOG.addHandler(loghdlr)  
        self.LOG.setLevel(logging.INFO) 

        self.SUCCESS = logging.getLogger('log.success')
        loghdlr1 = logging.handlers.RotatingFileHandler(filename=logPath+'/success.log', 
                                                        mode="a", maxBytes=maxBytes, backupCount=backupCount*2)   
        fmt1 = logging.Formatter("%(asctime)s %(message)s", "%Y-%m-%d %H:%M:%S")  
        loghdlr1.setFormatter(fmt1)  
        self.SUCCESS.addHandler(loghdlr1)  
        # self.SUCCESS.setLevel(logging.INFO)  
  
        self.FAIL = logging.getLogger('log.fail')  
        loghdlr2 = logging.handlers.RotatingFileHandler(filename=logPath+'/fail.log', 
                                                        mode="a", maxBytes=maxBytes, backupCount=backupCount)  
        fmt2 = logging.Formatter("%(asctime)s %(message)s", "%Y-%m-%d %H:%M:%S")  
        loghdlr2.setFormatter(fmt2)  
        self.FAIL.addHandler(loghdlr2)  
        # self.FAIL.setLevel(logging.INFO)
    # def error(self, msg):  
    #     if self.LOG is not None:  
    #         self.LOG.error(msg)  
    def info(self, msg):  
        if self.SUCCESS is not None:  
            self.SUCCESS.info(msg)
    # def debug(self, msg):  
    #     if self.FAIL is not None:  
    #         self.FAIL.debug(msg)
    # def fail(self, msg):  
    #     if self.FAIL is not None:  
    #         self.FAIL.debug(msg)  

    def error(self, msg):
        if self.FAIL is not None:  
            self.FAIL.error(msg) 

def main():  
    # global log_mgr  
    log_mgr = LogMgr()
    log_mgr.error('This is error log')      
    log_mgr.info('This is info log')      
    # log_mgr.debug('This is debug log')      
    # log_mgr.fail('This is fail log')   
  
if __name__ == "__main__":  
    main()  