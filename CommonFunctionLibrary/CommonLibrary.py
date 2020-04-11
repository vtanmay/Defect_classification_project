from jira.client import JIRA
import pandas as pd
import os
import xlwt
from xlwt import Workbook


# get defect summary from JIRA
def getDefectSummaryFromJira(prProject=None, prDefectId=None):
    key_list = []
    summary_list = []
    jira_options = {'server': 'https://servicedesk.oversightsystems.com'}
    jira = JIRA(options=jira_options, basic_auth=('tanmay.vaidya', 'l3tV41d41n!2019'))
    # project = 'WB' AND key in ('WB-3457', 'WB-3329')
    jql = 'project = {} AND key = {}'.format(prProject, prDefectId)
    issueList = jira.search_issues(jql)
    for issue in issueList:
        key_list.append(issue.key)
        summary_list.append(issue.fields.summary)
    return summary_list


def getColumnDataAsAListFromTable(prDataFrame=None, prOptColumnName=None, prOptColumnIndex=0):
    if prOptColumnName is not None:
        return prDataFrame[prOptColumnName].values.tolist()
    elif prOptColumnName is None:
        return prDataFrame[prDataFrame.columns[prOptColumnIndex]].values.tolist()


def getPerformanceKeywordsFromExcelSheet(prFilePath=None, prSheetName=None):
    df = readXLSFile(prFilePath, prSheetName)
    listData = getColumnDataAsAListFromTable(prDataFrame=df, prOptColumnIndex=0)
    return listData


def readXLSFile(prFilePath=None, prEitherSheetName=None, prOrSheetIndex=0):
    if prEitherSheetName is not None:
        df = pd.read_excel(prFilePath, sheet_name=prEitherSheetName)
        return df
    else:
        df = pd.read_excel(prFilePath, sheet_name=prOrSheetIndex)
        return df

def createXLSFileAndReturnXLSSheet(prWorkbookName='test.xls', prWorkbookSheet='test sheet'):
    wb = Workbook() # Workbook is created
    sheet = wb.add_sheet(prWorkbookSheet) # create sheet.
    style = xlwt.easyxf('font: bold 1')  # Specifying style
    sheet.write(0, 0, 'Defect id', style)
    sheet.write(0, 1, 'Defect type', style)
    #wb.get_sheet()
    wb.save(prWorkbookName)
    return wb


def getCurrentWorkingDirecotry():
    return os.getcwd()


def classifyDefect(prDefectId=None, prDefDetailsList=None, prRefKwList=None, prWb=None, prWorkbookName='test.xls'):
    for i in prRefKwList:
        for j in prDefDetailsList:
            if i.lower() in j.lower():
                sheet = prWb.get_sheet(0)
                sheet.write(1, 0, prDefectId)
                sheet.write(1, 1, 'Performance')
                prWb.save(prWorkbookName)
                #print("its a performance defect")
            else:
                sheet = prWb.get_sheet(0)
                sheet.write(1, 0, prDefectId)
                sheet.write(1, 1, 'Functional')
                prWb.save(prWorkbookName)
               # print("its a functional defect")
        break

