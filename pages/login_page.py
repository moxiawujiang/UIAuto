#coding=utf-8
__author__ = 'wujiang'
from public.BasePage import BasePage

#继承于Basepage
class LoginPage(BasePage):
    #元素定位信息
    _name="xpath://input[@placeholder='用户名']"
    _password="name:password"
    _login_botton="xpath://input[@value='登入']"

    def __init__(self, driver):
        BasePage.__init__(self, driver)
    '''
    元素定位层
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
    元素操作层
    '''
    #对用户名进行输入
    def sendkey_username(self,name):
        return  self.sendkey_element(self.get_username(),name)
    #对密码进行输入
    def sendkey_password(self,password):
        return  self.sendkey_element(self.get_password(),password)
    #点击登录按钮
    def click_login_button(self):
        return self.click_element(self.get_login_button())
    

    '''
    业务层
    '''
    #封装登录流程
    def login(self,username,password):
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
        list = ["无效证书"]
        for text in  list:
            self.check_exist_in_page(text)










