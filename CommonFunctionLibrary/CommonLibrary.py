from jira.client import JIRA
import pandas as pd

# get defect summary from JIRA
def getDefectSummaryFromJira(prProject=None, prDefectId=None):
    key_list = []
    summary_list = []
    jira_options = {'server': 'https://servicedesk.oversightsystems.com'}
    jira = JIRA(options=jira_options, basic_auth=('tanmay.vaidya', 'l3tV41d41n!2019'))
    jql = 'project = {} AND key = {}'.format(prProject,prDefectId)
    issueList = jira.search_issues(jql)
    for issue in issueList:
        key_list.append(issue.key)
        summary_list.append(issue.fields.summary)
    return summary_list

def getColumnDataAsAListFromTable(prDataFrame=None,prOptColumnName=None,prOptColumnIndex=0):
    if prOptColumnName is not None:
            return prDataFrame[prOptColumnName].values.tolist()
    elif prOptColumnName is None:
            return prDataFrame[prDataFrame.columns[prOptColumnIndex]].values.tolist()

def getPerformanceKeywordsFromExcelSheet(prFilePath=None, prSheetName=None):
        df = readXLSFile(prFilePath, prSheetName)
        listData = getColumnDataAsAListFromTable(prDataFrame=df, prOptColumnIndex=0)
        return listData

def readXLSFile(prFilePath=None,prEitherSheetName=None,prOrSheetIndex=0):
    if prEitherSheetName is not None:
       df=pd.read_excel(prFilePath,sheet_name=prEitherSheetName)
       return df
    else:
       df= pd.read_excel(prFilePath,sheet_name=prOrSheetIndex)
       return df