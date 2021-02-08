#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Created on 2021年2月8日
@author: jimmy
'''
from loguru import logger
import os

def logging(file_path):
	LOG_DIR = os.path.expanduser(file_path+"/logs")
	LOG_FILE = os.path.join(LOG_DIR,"file_{time:YYYY-MM-DD} .log")
	#创建日志路径
	if not os.path.exists(LOG_DIR):
		os.mkdir(LOG_DIR)
	#创建日志文件,文件超过200KB就压缩文件
	logger.add(LOG_FILE, rotation = "200KB", compression="zip")

	# logger.add("file_1.log", rotation="500 MB")    # Automatically rotate too big file
	# logger.add("file_2.log", rotation="12:00")     # New file is created each day at noon
	# logger.add("file_3.log", rotation="1 week")    # Once the file is too old, it's rotated
	# logger.add("file_X.log", retention="10 days")  # Cleanup after some time
	# logger.add("file_Y.log", compression="zip")    # Save some loved space

if __name__ == "__main__":
	logging('D:')

	logger.debug('this is a debug message')
	logger.info('this is another debug message')
	logger.warning('this is another debug message')
	logger.error('this is another debug message')
	logger.critical('this is critical message!')
	logger.success('this is success message!')