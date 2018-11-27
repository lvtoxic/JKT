# coding=utf-8

import unittest
from XX.unittest.init import *


def add(a, b):
    return a - b


class BaiduSo(Init):

    def test_001(self):
        # print(self.driver.title,type(self.driver.title))
        self.assertEquals(self.driver.title,'百度一下，你就知道')



    def test_002(self):
        so=self.driver.find_element_by_id('kw')
        # print(so.is_enabled())
        self.assertTrue(so.is_enabled())

    def test_003(self):
        self.assertIn('百度', self.driver.title)


if __name__ == '__main__':
    unittest.main(verbosity=2)
