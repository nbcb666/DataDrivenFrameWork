# -*- coding: utf-8 -*-
from ConfigParser import ConfigParser
from config.VarConfig import pageElementLocatorPath

#用于解析存储定位页面的定位表达式文件

class ParseCofigFile(object):

    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read(pageElementLocatorPath)

    def getItemsSection(self,sectionName):
        #获取配置文件中指定section下的所有option键值对
        #并以字典类型返回给调用者
        optionsDict = dict(self.cf.items(sectionName))
        return optionsDict

    def getOptionValue(self,sectionName,optionName):
        #获取指定section下的指定option的值
        value = self.cf.get(sectionName,optionName)
        return value

if __name__ == '__main__':
    pc = ParseCofigFile()
    print pc.getItemsSection("126mail_login")
    print pc.getOptionValue("126mail_login","loginPage.frame")