__author__ = '芜疆'
#coding=utf-8
import time
import unittest
import HTMLReport
import os
import sys
os.chdir(sys.path[0])

#收集测试用例
def create_my_suit():
    my_suit=unittest.TestSuite()
    testdir="test_case"
    discover=unittest.defaultTestLoader.discover(testdir,pattern="*case.py",top_level_dir=None)
    for test_suit in discover:
        for test_case in  test_suit:
            my_suit.addTest(test_case)
    return my_suit



if __name__ == '__main__':
    #执行测试
    time=time.strftime("%y-%m-%d %H-%M-%S")
    mysuit=create_my_suit()
    runner = HTMLReport.TestRunner(report_file_name='report'+time,
                                   output_path='report',
                                   title='测试报告',
                                   description='测试描述',
                                   lang='cn'  # 支持中文与英文，默认中文
                                   )
    runner.run(mysuit)
