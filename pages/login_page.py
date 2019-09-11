#coding=utf-8
__author__ = 'wujiang'
from public.BasePage import BasePage

class LoginPage(BasePage):
    _name="xpath://input[@placeholder='用户名']"
    _password="name:password"
    _login_botton="xpath://input[@value='登入']"

    def __init__(self,driver,url):
        BasePage.__init__(self,driver,url)

    #元素定位层
    def get_username(self):
         return self.find_element(self._name)

    def get_password(self):
        return  self.find_element(self._password)

    def get_login_button(self):
        return  self.find_element(self._login_botton)

    #元素操作层
    def sendkey_username(self,name):
        return  self.sendkey_element(self.get_username(),name)

    def sendkey_password(self,password):
        return  self.sendkey_element(self.get_password(),password)

    def click_login_button(self):
        return self.click_element(self.get_login_button())
    

    #业务层
    def login(self,username,password):
        self.open_bbrowser()
        self.sendkey_username(username)
        self.sendkey_password(password)
        self.click_login_button()








