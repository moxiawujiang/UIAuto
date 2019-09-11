_author__ = '芜疆'
#encoding=utf-8
from selenium import webdriver

#封装定位方式
class BasePage:
    def __init__(self,driver,url):
        self.driver=driver
        self.url=url

    def find_element(self,key):
         by = key.split(':')[0]
         by_value = key.split(":")[1]
         try:
            if by=='id':
                return self.driver.find_element_by_id(by_value)
            elif by=='name':
                return self.driver.find_element_by_name(by_value)
            elif by=="classname":
                return self.driver.find_element_by_class_name(by_value)
            elif by=="xpath":
                return self.driver.find_element_by_xpath(by_value)
            elif by=="css":
                return self.driver.find_element_by_css_selector(by_value)
            elif by=="linkname":
                return self.driver.find_element_by_link_name(by_value)
            elif by=="linktext":
                return self.driver.find_element_by_link_text(by_value)
            else:
                raise Exception("没有这种定位方式")
         except Exception as e:
             raise e
    def open_bbrowser(self):
        self.driver.get(self.url)

    def click_element(self,element):
        element.click()

    def sendkey_element(self,element,values):
        element.send_keys(values)



