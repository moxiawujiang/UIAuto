_author__ = '芜疆'
#encoding=utf-8
from selenium.webdriver.common.by import  By
from selenium.webdriver.support import  expected_conditions as EC
from  selenium.webdriver.support.ui import WebDriverWait

#封装定位方式
class BasePage:
    def __init__(self,driver,url):
        self.driver=driver
        if url==None:
            self.url='http://172.16.63.20/dashboard/auth/login/'
        else:
            self.url=url

    #封装定位方式
    def find_element(self,key):
         by = key.split(':')[0]
         by_value = key.split(":")[1]
         try:
            if by=='id':
                return WebDriverWait(self.driver,5,0.5).until(EC.presence_of_element_located((By.ID,by_value)))
            elif by=='name':
                return WebDriverWait(self.driver,5,0.5).until(EC.presence_of_element_located((By.NAME,by_value)))
            elif by=="classname":
                return WebDriverWait(self.driver,5,0.5).until(EC.presence_of_element_located((By.CLASS_NAME,by_value)))
            elif by=="xpath":
                return WebDriverWait(self.driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,by_value)))
            elif by=="css":
                return WebDriverWait(self.driver,5,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,by_value)))
            elif by=="linkname":
                return WebDriverWait(self.driver,5,0.5).until(EC.presence_of_element_located((By.LINK_TEXT,by_value)))
            elif by=="linktext":
                return WebDriverWait(self.driver,5,0.5).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,by_value)))
            else:
                raise Exception("没有这种定位方式")
         except Exception as e:
             raise e

    #打开浏览器
    def open_browser(self):
        self.driver.get(self.url)
    #点击元素
    def click_element(self,element):
        element.click()
    #元素输入
    def sendkey_element(self,element,values):
        element.send_keys(values)
    #获取元素的值
    def get_element_value(self,element):
        return element.text




