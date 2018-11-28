# coding=utf-8
import unittest
import time
import os
import HTMLTestRunner

'''
批量执行测试用例用discover
生成测试报告
'''


def allTests():
    suite = unittest.TestLoader().discover(start_dir=os.path.dirname(__file__), pattern='baidu_test*.py', top_level_dir=None)

    return suite

def getNowTime():
    return time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))



def run():
    fp = os.path.join(os.path.dirname(__file__), 'report', getNowTime()+'testReport.html')
    # unittest.TextTestRunner(verbosity=2).run(allTests())
    HTMLTestRunner.HTMLTestRunner(stream=open(fp,'wb'), title='自动化报告', description='详细信息').run(allTests())


if __name__ == '__main__':
    run()
