# -*- coding: utf-8 -*-
from pageObjects.HomePage import HomePage
from pageObjects.AddressBookPage import AddressBookPage
import traceback
import time
class AddContactPerson(object):
    def __init__(self):
        print "add contact person"

    @staticmethod
    def add(driver,contactName,contactEmail,isStar,contactPhone,contactComment):
        try:
            #创建主页实例
            hp = HomePage(driver)
            hp.addressLink().click()
            time.sleep(3)
            #创建联系人页面实例对象
            apb = AddressBookPage(driver)
            apb.createContactPersonButton().click()
            if contactName:
                #非必输项
                apb.contactPersonName().send_keys(contactName)
                #必输项
                apb.contactPersonEmail().send_keys(contactEmail)
            if isStar == u"是":
                apb.starContacts().click()
            if contactPhone:
                apb.contactPersonMoblie().send_keys(contactPhone)
            if contactComment:
                apb.contactPersonComment().send_keys(contactComment)
            apb.saveContacePerson().click()
        except Exception,e:
            print traceback.print_exc()
            raise e

if __name__ == '__main__':
    from LoginAction import LoginAction
    from selenium import webdriver
    import time

    driver = webdriver.Firefox(executable_path="C:\\wmh\\driver\\geckodriver")
    driver.get("https://mail.126.com")
    #driver.implicitly_wait(30)
    # 窗口最大化
    #driver.maximize_window()
    LoginAction.login(driver, "nbcb666", "nbcbnbcb")
    time.sleep(5)
    AddContactPerson.add(driver,u"楠楠","ersd2@qq.com",u"是","","")
    time.sleep(3)
    assert u"楠楠" in driver.page_source
    driver.quit()