# -*- coding: utf-8 -*-
from pageObjects.LoginPage import LoginPage

class LoginAction(object):
    def __init__(self):
        #self.driver = driver
        print u"login...."
    @staticmethod
    def login(driver,username,password):
        try:
            login = LoginPage(driver)
            login.changeTagObj().click()

            login.switchToFrame()
            login.userNameObj().send_keys(username)
            login.passwordObj().send_keys(password)
            login.loginButton().click()
            login.switchToDefaultFrame()
        except Exception,e:
            raise e

if __name__ == '__main__':
    from selenium import webdriver
    import time

    driver = webdriver.Firefox(executable_path="C:\\wmh\\driver\\geckodriver")
    driver.get("https://mail.126.com")
    time.sleep(5)
    #logina = LoginAction()
    LoginAction.login(driver,username = "nbcb666",password = "nbcbnbcb")
    time.sleep(5)
    driver.quit()