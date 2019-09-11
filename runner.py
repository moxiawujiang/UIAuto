from selenium import  webdriver
import time
from pages.login_page import LoginPage
class Test:
    def __init__(self):
        self.driver=webdriver.Chrome()
    def test(self):
        self.driver.get("http://www.baidu.com")
        time.sleep(3)
        self.driver.quit()
        element=self.driver.find_element_by_id("xxxx")
        element.send_keys()


if __name__ == '__main__':
    Test().test()