# coding=utf-8
__author__ = 'wujiang'
from public.BasePage import BasePage
from  unittest  import TestCase
import logging


# 继承于Basepage
class HomePage(BasePage):
    # 元素定位信息
    _mail_icon='id:_mail_icon_20_96'
    _name='id:msgboxAccountName'
    _loginout_button='xpath://span[text()="退出"]'

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    '''元素定位层'''
    #获取用户名元素
    def get_username(self):
        return self.find_element(self._name)
    #获取退出按钮
    def get_loginout_button(self):
        return self.find_element(self._loginout_button)

    '''元素操作层'''
    #点击用户信息显示小三角
    def click_mail_icon(self):
        self.click_element(self.find_element(self._mail_icon))
    #获取登录后的用户名
    def get_username_value(self):
        return self.get_element_value(self.get_username())
    #点击用户名
    def click_username(self):
        self.click_element(self.get_username())
    #点击退出按钮
    def click_loginout(self):
        self.click_element(self.get_loginout_button())

    '''业务层'''
    #校验用户名是否符合预期
    def check_username(self,expect):
        self.click_mail_icon()
        actual=self.get_username_value()
        logging.info("用户名：" + actual)
        TestCase().assertEqual(actual,expect)

    #封装退出流程
    def loginout(self):
        self.click_username()
        self.click_loginout()

















