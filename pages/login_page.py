#coding=utf-8
__author__ = 'wujiang'
from selenium.webdriver.common.by import By
from public.BasePage import BasePage
import time

#继承于Basepage
class LoginPage(BasePage):

    #元素定位信息
    _password_login=(By.ID,'switchAccountLogin')
    _name=(By.XPATH,'//input[@data-loginname="loginEmail"]')
    _password=(By.NAME,"password")
    _login_botton=(By.ID,"dologin")

    def __init__(self, driver):
        BasePage.__init__(self, driver)
    '''
    元素定位层--去掉元素定位层，原本的意义在于某一个元素可能会有单击、双击、右击等多种操作，所以封装元素定位能够复用，
    但是大多数元素都只有一个操作，很少存在多种操作，单独封装元素定位层，会比较冗余
    '''
    '''
    #获取用户名元素
    def get_username(self):
         return self.find_element(self._name)
    #获取密码元素
    def get_password(self):
        return  self.find_element(self._password)
    #获取登录按钮
    def get_login_button(self):
        return  self.find_element(self._login_botton)
    '''
    #获取iframe元素
    def get_login_iframe(self):
        self.find_element(self._login_iframe)

    '''
    元素操作层
    '''
    #点击密码登录连接
    def click_password_login(self):
        self.click_element(self.find_element(self._password_login))
    #对用户名进行输入
    def sendkey_username(self,name):
        self.sendkey_element(self.find_element(self._name),name)
    #对密码进行输入
    def sendkey_password(self,password):
        self.sendkey_element(self.find_element(self._password),password)
    #点击登录按钮
    def click_login_button(self):
        self.click_element(self.find_element(self._login_botton))
        time.sleep(1)

    

    '''
    业务层
    '''
    #封装登录流程
    def login(self,username,password):
        self.click_password_login()
        #切换iframe
        self.switch_to_frame(0)
        self.sendkey_username(username) #输入用户名
        self.sendkey_password(password) #输入密码
        self.click_login_button() # 点击登录按钮

    #检查是否在登录页面
    def check_isloginpage(self):
        list = ["用户名", '密码', '登入']
        for text in  list:
            self.check_exist_in_page(text)

    #登录失败校验
    def check_exist_failmsg(self):
        list = ["帐号或密码错误"]
        for text in  list:
            self.check_exist_in_page(text)










