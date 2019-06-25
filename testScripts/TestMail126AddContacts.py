# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from util.ParseExcel import ParseExcel
from config.VarConfig import *
from appModules.LoginAction import LoginAction
from appModules.AddContactPersonAction import AddContactPerson
import traceback
from time import sleep
from util.Log import *

#设置此次测试的环境编码utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#创建解析Excel对象
excelObj = ParseExcel()
#将excel文件加载到内存
excelObj.loadWorkBook(dataFilePath)

def LaunchBrowser():
    # #创建Chrome浏览器的一个options实例对象
    # chrome_options = Options()
    # #向options实例中添加禁用扩展插件的设置参数项
    # chrome_options.add_argument("--disable-extensions")
    # #添加屏蔽--ignore--certificate--errors提示信息的设置参数项
    # chrome_options.add_experimental_option\
    #     ("excludeSwitches",["ignore-certificate-errors"])
    # #添加浏览器最大化的设置参数项，已启动最大化
    # chrome_options.add_argument('--start-maximized')
    # #启动带有自定义设置的chrome浏览器
    # driver = webdriver.Chrome\
    #     (executable_path="C:\\wmh\\driver\\chromedriver",chrome_options = chrome_options)
    # #访问126邮箱首页
    driver = webdriver.Firefox(executable_path="C:\\wmh\\driver\\geckodriver")
    driver.get("http://mail.126.com")
    sleep(3)
    return driver

def test126MailAddContacts():
    logging.info(u"126邮箱添加联系人数据驱动测试开始。。。。")
    try:
        #根据excel文件中的Sheet名称获取此Sheet对象
        userSheet = excelObj.getSheetByName(u"126账号")
        #获取126账号sheet中是否执行列
        isExecuteUser = excelObj.getColumn(userSheet,account_isExecute)

        #获取sheet表中的数据表列
        dataBookColumn = excelObj.getColumn(userSheet,account_dataBook)
        print u"测试为126邮箱添加联系人执行开始。。。。"

        for idx,i in enumerate(isExecuteUser[1:]):
            #循环遍历126账号表中的账号，为需要执行的账号添加联系人
            if i== "y":
                #获取第i行数据 从第二行开始才有数据
                userRow = excelObj.getRow(userSheet,idx+2)
                print userRow
                #获取第i行中的用户名
                username = userRow[account_username-1]
                print username
                # 获取第i行中的密码
                password = str(userRow[account_password-1])
                print username,password

                #创建浏览器实例对象
                driver = LaunchBrowser()
                logging.info(u"驱动浏览器，访问126邮箱主页")
                sleep(3)

                #登录126邮箱
                LoginAction.login(driver, username, password)
                sleep(5)
                try:
                    assert u"收 信" in driver.page_source
                    logging.info\
                        (u"用户%s登录后，断言页面关键字 收信 成功" %username)
                except AssertionError,e:
                    logging.debug(u"用户%s登录后，页面断言关键字 收信 失败，"
                                  u"异常信息：%s" %(username,str(traceback.format_exc())))
                #获取为第i行中用户添加的联系人数据sheet名
                dataBookName = dataBookColumn[idx +1]
                #获取对应的数据表对象
                dataSheet = excelObj.getSheetByName(dataBookName)
                #获取联系人数据表中是否执行列对象
                isExecuteUser = excelObj.getColumn(dataSheet,contacts_isExecute)
                contactNum = 0 #记录添加成功联系人 个数
                isExecuteNum = 0 #记录需要执行联系人个数
                for id ,data in enumerate(isExecuteUser[1:]):
                    #循环遍历是否执行添加联系人列,
                    #如果被设置为添加，则进行联系人添加
                    if data== "y":
                        #如果id行的联系人被设置为执行，则isExecuteNum+1
                        isExecuteNum +=1
                        #获取联系人表地第id+2行对象
                        rowContent = excelObj.getRow(dataSheet,id+2)
                        #获取联系人信息
                        contactPersonName= \
                            rowContent[contacts_contactPersonName-1]
                        #获取联系人邮箱
                        contactPersonEmail = \
                            rowContent[contacts_contactPersonEmail-1]
                        isStar = \
                            rowContent[contacts_isStar-1]
                        contactPersonPhone = \
                            rowContent[contacts_contactPersonMobile-1]
                        contactPersonComment = \
                            rowContent[contacts_contactPersonComment-1]
                        assertKeyWord = \
                            rowContent[contacts_assertKeyWords-1]

                        print contactPersonName,contactPersonEmail,assertKeyWord
                        print contactPersonPhone,contactPersonComment,isStar
                        #执行新建联系人操作
                        AddContactPerson.add(driver,
                                             contactPersonName,
                                             contactPersonEmail,
                                             isStar,
                                             contactPersonPhone,
                                             contactPersonComment)
                        sleep(1)
                        logging.info(u"添加联系人%s成功" % contactPersonEmail)
                        #在联系人工作表中写入添加联系人执行时间
                        excelObj.writeCellCurrentTime(dataSheet,
                                                      rowNo=id+2,colsNo=contacts_runTime)
                        try:
                            #断言给定的关键字是否出现在页面中
                            assert assertKeyWord in driver.page_source
                        except AssertionError,e:
                            #断言失败，在联系人工作表中写入添加联系人测试失败信息
                            excelObj.writeCell(dataSheet,"faild",rowNo=id+2,
                                               colsNo= contacts_testResult,style = 'red')
                            logging.info(u"断言关键字 %s失败" % assertKeyWord)
                        else:
                            #断言成功，写入添加联系人成功过信息
                            excelObj.writeCell(dataSheet,"pass",rowNo=id+2,
                                               colsNo=contacts_testResult,style="green")
                            contactNum +=1
                            logging.info(u"断言关键字 %s 成功" % assertKeyWord)
                # print "contactNum = %s, isExecuteNum = %s"\
                #     %(contactNum,isExecuteNum)
                    else:
                        logging.info(u"联系人%s被忽略执行" %contactPersonEmail)
                if contactNum == isExecuteNum:
                    excelObj.writeCell(dataSheet, "pass", rowNo=id + 2,
                                        colsNo=account_testResult, style="green")
                    #print u"为用户%s添加%d个联系人，，测试通过" \
                        #  % (contactNum, isExecuteNum)
                else:
                    excelObj.writeCell(dataSheet, "failed", rowNo=id + 2,
                                        colsNo=account_testResult, style="red")
                    logging.info(u"为用户%s添加%d个联系人，%d个成功\n"\
                                 %(username,isExecuteNum,contactNum))
            else:
                ignoreUserName =excelObj.getCellOfValues(userSheet,
                                                         rowNo = idx+2,colsNo = account_username)
                logging.info(u"用户%s被忽略执行\n" %ignoreUserName)
            driver.quit()


    except Exception,e:
        logging.debug(u"数据驱动框架主程序发生异常，异常信息为：%s"\
                      %str(traceback.format_exc()))


if __name__ == '__main__':
    test126MailAddContacts()
    print u"登录126邮箱成功"


