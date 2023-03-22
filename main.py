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
        logging.debug('修改This is a debug message修改1')
        logging.info('修改This is an info message修改1')
        logging.warning('修改This is a warning message修改1')
        logging.error('修改This is an error message修改1')
        logging.critical('修改This is a critical message修改1')
        time.sleep(3)


if __name__ == '__main__':
    start()
