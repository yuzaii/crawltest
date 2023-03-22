import time

import requests
import logging

# 设置日志级别为DEBUG
logging.basicConfig(level=logging.DEBUG)


# 记录不同级别的日志信息


def start():
    for i in range(10):
        # res = requests.get('http://127.0.0.1:6060/post/postcategory')
        # print(res.text)
        logging.debug('This is a debug message')
        logging.info('This is an info message')
        logging.warning('This is a warning message')
        logging.error('This is an error message')
        logging.critical('This is a critical message')
        time.sleep(3)


if __name__ == '__main__':
    start()