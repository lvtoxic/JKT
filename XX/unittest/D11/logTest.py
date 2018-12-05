# coding=utf-8

import logging
import unittest
from selenium import webdriver

def log(log_content):
    # 定义文件
    logFile = logging.FileHandler('log.md', 'a',encoding='utf-8')
    # log格式
    fmt = logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s')
    logFile.setFormatter(fmt)
    # 定义日志
    logger1 = logging.Logger('logTest', level=logging.DEBUG)
    logger1.addHandler(logFile)
    logger1.info(log_content)


# log('阿斯顿')

class Ui(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        log('初始化浏览器')

    def test_01(self):
        log('开始测试')
        pass

    def tearDown(self):
        log('关闭浏览器')
        self.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity=2)