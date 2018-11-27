# coding=utf-8
from selenium import webdriver
import unittest
import time


class BaiduTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.driver.get('http://www.baidu.com')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_baidu_news(self):
        self.driver.find_element_by_link_text('新闻').click()
        self.driver.back()

    def test_baidu_maps(self):
        self.driver.find_element_by_partial_link_text('图').click()
        self.driver.back()


if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(BaiduTest('tearDownClass'))
    # suite.addTest(BaiduTest('test_baidu_maps'))
    # unittest.TextTestRunner(verbosity=2).run(suite)
