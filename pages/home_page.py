# coding=utf-8
__author__ = 'wujiang'
from public.BasePage import BasePage
from  unittest  import TestCase
import logging


# 继承于Basepage
class HomePage(BasePage):
    # 元素定位信息
    _name='xpath://p[@class="user_box"]//span[1]'
    _loginout_button='xpath://span[text()="退出"]'

    def __init__(self, driver, url=None):
        BasePage.__init__(self, driver, url)

    '''元素定位层'''
    #获取用户名元素
    def get_username(self):
        return self.find_element(self._name)
    #获取退出按钮
    def get_loginout_button(self):
        return self.find_element(self._loginout_button)

    '''元素操作层'''
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
        actual=self.get_username_value()
        logging.info("用户名：" + actual)
        TestCase().assertEqual(actual,expect)

    #校验角色权限
    def check_user_auth(self,role):
        list=["系统控制台",'资源','租户']
        #1为admin角色
        for text in list:
            if role==1:
                TestCase().assertTrue( text in self.driver.page_source)
            else:
                TestCase().assertFalse(text in self.driver.page_source)
    #封装退出流程
    def loginout(self):
        self.click_username()
        self.click_loginout()

















