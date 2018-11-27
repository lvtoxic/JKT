# coding=utf-8

import unittest
from selenium import webdriver


class BaiduLink(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get('http://www.baidu.com')

    def tearDown(self):
        self.driver.quit()

    def test_001(self):
        self.driver.find_element_by_link_text('新闻').click()

    def test_002(self):
        self.driver.find_element_by_link_text('地图').click()

    @staticmethod
    def suite():
        suite = unittest.TestSuite(unittest.makeSuite(BaiduLink))
        return suite

if __name__ == '__main__':
    '''测试套件分离'''
    unittest.TextTestRunner(verbosity=2).run(BaiduLink.suite())
