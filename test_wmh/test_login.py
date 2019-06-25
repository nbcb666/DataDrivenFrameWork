# -*- coding: utf-8 -*-
from appModules.LoginAction import LoginAction

from util.ParseExcel import ParseExcel
from config.VarConfig import *

if __name__ =="__main__":
    from selenium import webdriver
    import time

    # 创建解析Excel对象
    excelObj = ParseExcel()
    # 将excel文件加载到内存
    excelObj.loadWorkBook(dataFilePath)

    # 根据excel文件中的Sheet名称获取此Sheet对象
    userSheet = excelObj.getSheetByName(u"126账号")
    # 获取126账号sheet中是否执行列
    isExecuteUser = excelObj.getColumn(userSheet, account_isExecute)

    for idx, i in enumerate(isExecuteUser[1:]):
        # 循环遍历126账号表中的账号，为需要执行的账号添加联系人
        if i == "y":
            # 获取第i行数据 从第二行开始才有数据
            userRow = excelObj.getRow(userSheet, idx + 2)
            print userRow
            # 获取第i行中的用户名
            username = userRow[account_username - 1]
            print username
            # 获取第i行中的密码
            password = str(userRow[account_password - 1])
            print username, password

            driver = webdriver.Firefox(executable_path="C:\\wmh\\driver\\geckodriver")
            driver.get("https://mail.126.com")
            time.sleep(5)
            LoginAction.login(driver,username,password)
            time.sleep(5)
            driver.quit()