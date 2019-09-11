#coding=utf-8
__author__ = 'wujiang'
import unittest
import logging
from selenium import webdriver
from pages.login_page import LoginPage
from pages.home_page import HomePage

class LoginTest(unittest.TestCase):
    '''登录测试'''
    driver = webdriver.Chrome()
    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    #登录测试
    def test_login001(self,):
        '''登录成功'''
        LoginPage(self.driver,url='').login('','')
        #获取登录后的用户名
        username=HomePage(self.driver,url='').get_username_value()
        logging.info("用户名："+username)
        self.assertEqual('admin',username) #校验登录后的用户名是否正确



if __name__ == '__main__':
    unittest.main()