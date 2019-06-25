# -*- coding: utf-8 -*-
from util.ObjectMap import *

class LoginPage(object):
    def __init__(self,driver):
        self.driver = driver

    def switchToFrame(self):
        self.driver.switch_to.frame(3)

    def switchToDefaultFrame(self):
        self.driver.switch_to.default_content()

    def changeTagObj(self):
        try:
            #获取登录页面的用户名输入框页面对象，并返回给调用者
            elementObj = getElement(self.driver,"xpath","//div[@id='lbNormal']")
            return elementObj
        except Exception,e:
            raise e


    def userNameObj(self):
        try:
            #获取登录页面的用户名输入框页面对象，并返回给调用者
            elementObj = getElement(self.driver,"xpath","//input[@name='email']")
            return elementObj
        except Exception,e:
            raise e

    def passwordObj(self):
        try:
            # 获取登录页面的密码输入框页面对象，并返回给调用者
            elementObj = getElement(self.driver,"xpath","//input[@name='password']")
            return elementObj
        except Exception,e:
            raise e

    def loginButton(self):
        try:
            # 获取登录页面的密码输入框页面对象，并返回给调用者
            elementObj = getElement(self.driver,"id","dologin")
            return elementObj
        except Exception,e:
            raise e

if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Firefox(executable_path="C:\\wmh\\driver\\geckodriver")
    driver.get("https://mail.126.com")
    import time
    time.sleep(5)
    login = LoginPage(driver)
    login.changeTagObj().click()
    time.sleep(2)
    driver.switch_to.frame(3)
    login.userNameObj().send_keys("nbcb666")
    login.passwordObj().send_keys("nbcbnbcb")
    login.loginButton().click()
    login.switchToDefaultFrame()
    driver.quit()