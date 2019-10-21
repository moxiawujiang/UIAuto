#coding=utf-8
__author__ = 'wujiang'
from HTMLReport import AddImage


#添加截图到报告中去
def get_screen_add_report(driver):
    image=driver.get_screenshot_as_base64()
    AddImage(image)


#截图装饰器
def get_screen_in_case_end_or_error(func):
    def f1(obj,*args,**kwargs):
        try:
            func(obj,*args,**kwargs)
            get_screen_add_report(obj.driver)
            obj.driver.refresh()
        except:
            get_screen_add_report(obj.driver)
            obj.driver.refresh()
            raise
    return f1
