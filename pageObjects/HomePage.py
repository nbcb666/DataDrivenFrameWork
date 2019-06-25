# -*- coding: utf-8 -*-
from util.ObjectMap import *
from util.ParseConfigurationFile import ParseCofigFile


class HomePage(object):

    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseCofigFile()

    def addressLink(self):
        try:
            #从定位表达式配置文件读取定位通讯录按钮的定位方式和表达式
            locateType, locatorExpression = self.parseCF.getOptionValue\
                    ("126mail_homePage","homePage.addressbook").split(">")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception, e:
            raise e