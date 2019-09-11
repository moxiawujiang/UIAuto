__author__ = '芜疆'
#coding=utf-8

import unittest
import HTMLReport
import os
import sys
os.chdir(sys.path[0])


def create_my_suit():
    my_suit=unittest.TestSuite()
    testdir="test_case"
    discover=unittest.defaultTestLoader.discover(testdir,pattern="*case.py",top_level_dir=None)
    for test_suit in discover:
        for test_case in  test_suit:
            my_suit.addTest(test_case)
    return my_suit

if __name__ == '__main__':
    mysuit=create_my_suit()
    runner = HTMLReport.TestRunner(report_file_name='UI自动化测试报告',
                                   output_path='report',
                                   title='测试报告',
                                   description='测试描述',
                                   thread_count=1,  # 并发线程数量（无序执行测试），默认数量 1
                                   thread_start_wait=3,  # 各线程启动延迟，默认 0 s
                                   sequential_execution=True,  # 是否按照套件添加(addTests)顺序执行，
                                   # 会等待一个addTests执行完成，再执行下一个，默认 False
                                   # 如果用例中存在 tearDownClass ，建议设置为True，
                                   # 否则 tearDownClass 将会在所有用例线程执行完后才会执行。
                                   lang='cn'  # 支持中文与英文，默认中文
                                   )
    runner.run(mysuit)