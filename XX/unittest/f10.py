# coding=utf-8

import unittest
from XX.unittest.init import *


class BaiduSo(Init):
    '''
    分离测试固件,固件存在init.py文件中
    '''

    def test_baidu_news(self):
        self.driver.find_element_by_id('kw').send_keys('webdriver')


if __name__ == '__main__':
    unittest.main(verbosity=2)
