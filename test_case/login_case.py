#coding=utf-8
__author__ = 'wujiang'
from selenium import webdriver
import unittest
from ddt  import *
from public.BasePage import BasePage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from  public.public import get_screen_in_case_end_or_error


@ddt
class LoginTest(unittest.TestCase):
    '''登录测试'''
    def  setUp(self):
        self.driver =webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        BasePage(self.driver).visit_url()

    def tearDown(self) :
        self.driver.quit()

    #登录测试
    @data(("user002","user003"),("user003","user003"))
    @unpack
    @get_screen_in_case_end_or_error
    def test_login001(self,username,password):
        self._testMethodDoc='''普通用户登录成功'''
        LoginPage(self.driver).login(username,password)
        #校验登录后的用户名
        HomePage(self.driver).check_username(username)
        #校验登录后没有控制台权限
        HomePage(self.driver).check_user_auth(2)


    @get_screen_in_case_end_or_error
    def test_login002(self):
        self._testMethodDoc='''admin用户登录成功'''
        LoginPage(self.driver).login('admin','admin')
        #校验登录后的用户名
        HomePage(self.driver).check_username('admin')
        #校验登录后没有控制台权限
        HomePage(self.driver).check_user_auth(1)


    @data((123456,123456),("user002",'123456'))
    @unpack
    @get_screen_in_case_end_or_error
    def test_login003(self,username,password):
        self._testMethodDoc='''登录失败'''
        LoginPage(self.driver).login(username, password)
        #校验存在登录失败的提示信息
        LoginPage(self.driver).check_exist_failmsg()

    @get_screen_in_case_end_or_error
    def test_loginout(self):
        self._testMethodDoc='''退出登录'''
        #用户登录
        LoginPage(self.driver).login('user002', 'user003')
        #用户退出
        HomePage(self.driver).loginout()
        #检查是否在登录页面
        LoginPage(self.driver).check_isloginpage()


if __name__ == '__main__':
    unittest.main()
