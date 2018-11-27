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


class BaiduSo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get('http://www.baidu.com')

    def tearDown(self):
        self.driver.quit()

    def test_baidu_news(self):
        self.driver.find_element_by_id('kw').send_keys('webdriver')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase('f8.py')
    unittest.TextTestRunner(verbosity=2).run(suite)
