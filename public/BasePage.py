_author__ = '芜疆'
#encoding=utf-8
from selenium.webdriver.common.by import  By
from selenium.webdriver.support import  expected_conditions as EC
from  selenium.webdriver.support.ui import WebDriverWait
from  unittest import TestCase

class BasePage:
    def __init__(self,driver):
        self.driver =driver

    #封装定位方式
    def find_element(self,*args):
         try:
             return WebDriverWait(self.driver, 5, 0.5).until(EC.visibility_of_element_located(*args))
         except Exception as e:
             raise e
    def  find_elements(self,*loc):
        try:
            return WebDriverWait(self.driver, 5, 0.5).until(EC.visibility_of_any_elements_located(*loc))
        except Exception as e:
            raise e

    #打开网址
    def visit_url(self,url=None):
        if url==None:
            url='。。。'
        else:
            url=url
        self.driver.get(url)

    '''元素操作封装 '''
    #点击元素
    def click_element(self,element):
        element.click()
    #元素输入
    def sendkey_element(self,element,values):
        element.send_keys(values)
    #获取元素的值
    def get_element_value(self,element):
        return element.text
    #清空元素
    def clear_element(self,element):
        element.clear()
    #获取某个元素的属性
    def get_element_attribute(self,element,attribute):
        return element.get_attribute(attribute)

    '''断言封装'''
    #校验是否为真
    def assert_True(self,key):
        TestCase().assertTrue(key)
    #校验是否为假
    def assert_False(self,key):
        TestCase().assertFalse(key)
    #校验是否相等
    def assert_Equal(self,key1,key2):
        TestCase().assertEqual(key1,key2)
    #校验是否不相等
    def assert_Not_Equal(self,key1,key2):
        TestCase().assertNotEqual(key1,key2)
    #校验页面是否存在某字符串
    def check_exist_in_page(self,str):
        self.assert_True( str in self.driver.page_source)
