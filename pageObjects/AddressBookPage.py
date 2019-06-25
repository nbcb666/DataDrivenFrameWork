# -*- coding: utf-8 -*-
from util.ObjectMap import *
from util.ParseConfigurationFile import ParseCofigFile


class AddressBookPage(object):

    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseCofigFile()
        self.addContactsOptions = self.parseCF.getItemsSection("126mail_addContactsPage")
        print self.addContactsOptions

    def createContactPersonButton(self):
        #获取新建联系人按钮
        try:
            locateType, locatorExpression = self.addContactsOptions\
                   ["addContactsPage.createContactsBtn".lower()].split(">")
            # 获取登录页面的用户名输入框页面对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception, e:
            raise e

    def contactPersonName(self):
        # h获取姓名输入框
        try:
            locateType, locatorExpression = self.addContactsOptions \
                ["addContactsPage.createPersonName".lower()].split(">")
            # 获取登录页面的姓名输入框页面对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception, e:
            raise e

    def contactPersonEmail(self):
        # 获取邮箱输入框
        try:
            locateType, locatorExpression = self.addContactsOptions \
                ["addContactsPage.createPersonEmail".lower()].split(">")
            # 获取登录页面的邮箱输入框页面对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception, e:
            raise e

    def starContacts(self):
        # 获取星标联系人
        try:
            locateType, locatorExpression = self.addContactsOptions \
                ["addContactsPage.starContacts".lower()].split(">")
            # 获取登录页面的邮箱输入框页面对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception, e:
            raise e

    def contactPersonMoblie(self):
        # 获取手机号输入框
        try:
            locateType, locatorExpression = self.addContactsOptions \
                ["addContactsPage.createPersonMobile".lower()].split(">")
            # 获取登录页面的邮箱输入框页面对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception, e:
            raise e

    def contactPersonComment(self):
        # 获取备注信息输入框
        try:
            locateType, locatorExpression = self.addContactsOptions \
                ["addContactsPage.createPersonComment".lower()].split(">")
            # 获取登录页面的邮箱输入框页面对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception, e:
            raise e

    def saveContacePerson(self):
        # 获取保存联系人按钮
        try:
            locateType, locatorExpression = self.addContactsOptions \
                ["addContactsPage.savecontacePerson".lower()].split(">")
            # 获取登录页面的邮箱输入框页面对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception, e:
            raise e

