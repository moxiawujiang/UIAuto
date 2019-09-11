#coding=utf-8
__author__ = 'wujiang'
import unittest
from selenium import webdriver
from pages.login_page import LoginPage

class LoginTest(unittest.TestCase):

    driver = webdriver.Chrome()
    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login001(self):
        LoginPage(self.driver,url='').login('','')



if __name__ == '__main__':
    unittest.main()