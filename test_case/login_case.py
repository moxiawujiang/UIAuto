#coding=utf-8
__author__ = 'wujiang'
import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.home_page import HomePage
from ddt  import *

@ddt
class LoginTest(unittest.TestCase):
    '''登录测试'''
    def  setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    def tearDown(self) :
        self.driver.quit()

    #登录测试
    @data(("user002","user003"),("user003","user003"))
    @unpack
    def test_login001(self,username,password):
        '''普通用户登录成功'''
        LoginPage(self.driver).login(username,password)
        #校验登录后的用户名
        HomePage(self.driver).check_username(username)
        #校验登录后没有控制台权限
        HomePage(self.driver).check_user_auth(2)

    def test_login002(self):
        '''admin用户登录成功'''
        LoginPage(self.driver).login('admin','longyuan!')
        #校验登录后的用户名
        HomePage(self.driver).check_username('admin')
        #校验登录后没有控制台权限
        HomePage(self.driver).check_user_auth(1)
    @data((None,None),(123456,123456),("user002",'123456'))
    @unpack
    def test_login003(self,username,password):
        '''登录失败'''
        LoginPage(self.driver).login(username, password)
        #校验存在登录失败的提示信息
        LoginPage(self.driver).check_exist_failmsg()

    def test_loginout(self):
        '''退出登录'''
        #用户登录
        LoginPage(self.driver).login('user002', 'user002')
        #用户退出
        HomePage(self.driver).loginout()
        #检查是否在登录页面
        LoginPage(self.driver).check_isloginpage()










if __name__ == '__main__':
    unittest.main()