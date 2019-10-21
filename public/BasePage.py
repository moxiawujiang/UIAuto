_author__ = '芜疆'
#encoding=utf-8
from selenium.webdriver.common.by import  By
from selenium.webdriver.support import  expected_conditions as EC
from  selenium.webdriver.support.ui import WebDriverWait
from  unittest import TestCase
from selenium import webdriver

#封装定位方式
class BasePage:
    def __init__(self,browser='chrome'):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)

    #封装定位方式
    def find_element(self,key):
         by = key.split(':')[0]
         by_value = key.split(":")[1]
         try:
            if by=='id':
                return WebDriverWait(self.driver,5,0.5).until(EC.visibility_of_element_located((By.ID,by_value)))
            elif by=='name':
                return WebDriverWait(self.driver,5,0.5).until(EC.visibility_of_element_located((By.NAME,by_value)))
            elif by=="classname":
                return WebDriverWait(self.driver,5,0.5).until(EC.visibility_of_element_located((By.CLASS_NAME,by_value)))
            elif by=="xpath":
                return WebDriverWait(self.driver,5,0.5).until(EC.visibility_of_element_located((By.XPATH,by_value)))
            elif by=="css":
                return WebDriverWait(self.driver,5,0.5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,by_value)))
            elif by=="linkname":
                return WebDriverWait(self.driver,5,0.5).until(EC.visibility_of_element_located((By.LINK_TEXT,by_value)))
            elif by=="linktext":
                return WebDriverWait(self.driver,5,0.5).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT,by_value)))
            else:
                raise Exception("没有这种定位方式")
         except Exception as e:
             raise e

    def  find_elements(self,key):
        by = key.split(':')[0]
        by_value = key.split(":")[1]
        try:
            if by == 'id':
                return WebDriverWait(self.driver, 5, 0.5).until(EC.visibility_of_any_elements_located((By.ID, by_value)))
            elif by == 'name':
                return WebDriverWait(self.driver, 5, 0.5).until(EC.visibility_of_any_elements_located((By.NAME, by_value)))
            elif by == "classname":
                return WebDriverWait(self.driver, 5, 0.5).until(EC.visibility_of_any_elements_located((By.CLASS_NAME, by_value)))
            elif by == "xpath":
                return WebDriverWait(self.driver, 5, 0.5).until(EC.visibility_of_any_elements_located((By.XPATH, by_value)))
            else:
                raise Exception("没有这种定位方式")
        except Exception as e:
            raise e


    #打开网址
    def visit_url(self,url=None):
        if url==None:
            url='http://172.16.63.20/dashboard/auth/login/'
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
