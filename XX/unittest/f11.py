# coding=utf-8

import unittest
from XX.unittest.init import *


def add(a,b):
    return a-b

class BaiduSo(Init):


    @unittest.skip('忽略这条测试用例')
    def test_001(self):
        self.driver.find_element_by_link_text('新闻').click()

    def test_002(self):
        self.driver.find_element_by_link_text('地图').click()

    @unittest.expectedFailure#预期的失败
    def test_003(self):
        self.assertEquals(add(2,3),1)

if __name__ == '__main__':
    unittest.main(verbosity=2)
