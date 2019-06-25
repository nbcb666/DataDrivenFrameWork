# -*- coding: utf-8 -*-
import openpyxl
from openpyxl.styles import Border,Side,Font
import time

class ParseExcel(object):

    def __init__(self):
        self.workbook = None
        self.excelFile = None
        self.Font = Font(color=None)#设置字体颜色
        #颜色对应的RGB值
        self.RGBDict = {'red':'FFFF3030','green':'FF008B00'}

    def getRow(self,sheet,rowNo):
        for row in sheet.rows:  # 返回的row是一个tuple对象
            for cell in row:
                # print 'row: %s  column: %s  value: %s' % (cell.row,cell.column,cell.value)
                if cell.row == rowNo:
                    #print 'row: %s  column: %s  value: %s' % (cell.row, cell.column, cell.value)
                    return cell.row, cell.column, cell.value


    def getColumn(self,sheet,colNo):
        for col in sheet.rows:  # 返回的row是一个tuple对象
            for cell in col:
                # print 'row: %s  column: %s  value: %s' % (cell.row,cell.column,cell.value)
                if cell.column == colNo:
                    #print 'row: %s  column: %s  value: %s' % (cell.row,cell.column,cell.value)
                    return col

    def getSheetByIndex(self,sheetIndex):
        #根据sheet的索引号获取该sheet对象
        try:
            sheetname = self.workbook.get_sheet_names()[sheetIndex]
        except Exception,e:
            raise e
        sheet = self.workbook.get_sheet_by_name(sheetname)
        return sheet

    def loadWorkBook(self,excelPathAndName):
        #将Excel文件加载到内存，并获取其workbook对象
        try:
            self.workbook = openpyxl.load_workbook(excelPathAndName)
        except Exception,e:
            raise e
        self.excelFile = excelPathAndName
        return self.workbook


if __name__ == '__main__':
    pe = ParseExcel()
    pe.loadWorkBook(u'C:\\wmh\\DataDrivenFrameWork\\testData\\126邮箱联系人.xlsx')
    sheet = pe.getSheetByIndex(0)
    #rows = pe.getRow(sheet, 1)  # 获取第一行
    print "^^^^^^^^^^^^^^^^^^^6"
    cols = pe.getColumn(sheet,1)
    print cols

