# coding=utf-8
__author__ = 'wujiang'
from public.BasePage import BasePage


# 继承于Basepage
class HomePage(BasePage):
    # 元素定位信息
    _name='xpath://p[@class="user_box"]//span[1]'

    def __init__(self, driver, url):
        BasePage.__init__(self, driver, url)

    # 元素定位层
    def get_username(self):
        print(self._name)
        return self.find_element(self._name)

    # 元素操作层
    def get_username_value(self):
        return self.get_element_value(self.get_username())










