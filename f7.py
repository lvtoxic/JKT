# coding=utf-8

import unittest
from selenium import webdriver


class F7(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_001(self):
        pass

    def test_002(self):
        pass


if __name__ == '__main__':
    suite = unittest.TestSuite(unittest.makeSuite(F7))
    unittest.TextTestRunner(verbosity=2).run(suite)
