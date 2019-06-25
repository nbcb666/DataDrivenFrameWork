# -*- coding: utf-8 -*-
from util.ObjectMap import *
from util.ParseConfigurationFile import ParseCofigFile

class LoginPage(object):
    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseCofigFile()
        self.loginOptions = self.parseCF.getItemsSection("126mail_login")
        print self.loginOptions

    def switchToFrame(self):
        self.driver.switch_to.frame(3)

    def switchToDefaultFrame(self):
        try:
            self.driver.switch_to.default_content()
        except Exception,e:
            raise e

    def changeTagObj(self):
        try:
            locateType,locatorExpression = self.loginOptions\
            ["loginPage.changetag".lower()].split(">")
            #获取登录页面的用户名输入框页面对象，并返回给调用者
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception,e:
            raise e


    def userNameObj(self):
        try:
            #从定位表达式配置文件中读取定位用户名输入框的定位方式和表达式
            locateType,locatorExpression = self.loginOptions\
            ["loginPage.username".lower()].split(">")
            #获取登录页面的用户名输入框页面对象，并返回给调用者
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception,e:
            raise e

    def passwordObj(self):
        try:
            locateType,locatorExpression = self.loginOptions\
            ["loginPage.password".lower()].split(">")
            # 获取登录页面的密码输入框页面对象，并返回给调用者
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception,e:
            raise e

    def loginButton(self):
        try:
            locateType,locatorExpression = self.loginOptions\
            ["loginPage.loginbutton".lower()].split(">")
            # 获取登录页面的密码输入框页面对象，并返回给调用者
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception,e:
            raise e

if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Firefox(executable_path="C:\\wmh\\driver\\geckodriver")
    driver.get("https://mail.126.com")
    import time
    time.sleep(2)
    login = LoginPage(driver)
    login.changeTagObj().click()
    time.sleep(2)
    login.switchToFrame()
    login.userNameObj().send_keys("nbcb666")
    login.passwordObj().send_keys("nbcbnbcb")
    login.loginButton().click()
    login.switchToDefaultFrame()
    #assert u"未读邮件" in driver.page_source
    driver.quit()