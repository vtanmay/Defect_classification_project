import CommonFunctionLibrary.CommonLibrary as cmnLib

# fetch defect data from JIRA - WB-2908-P, WB-3201-NP, WB-2806-P, WB-3202-NP
projectId = 'WB'
defectId = 'WB-2806'
defectSummary = cmnLib.getDefectSummaryFromJira(prProject=projectId, prDefectId=defectId)
defectDescription = cmnLib.getDefectDescriptionFromJira(prDefectId=defectId)
# read performance keywords data from excel.
loc = (cmnLib.getCurrentWorkingDirecotry()+"\Reference_keywords.xlsx")
listOfPerfKeywords = cmnLib.getPerformanceKeywordsFromExcelSheet(prFilePath=loc, prSheetName='Performance Keywords')
# create Excel file.
wb = cmnLib.createXLSFileAndReturnXLSWb(prWorkbookName='Classified_defects.xls', prWorkbookSheet='classified defects')
# classify defect.
flag = cmnLib.classifyDefect(prDefSummary=defectSummary, prDefDescr=defectDescription, prRefKwList=listOfPerfKeywords)
# write result to excel.
cmnLib.writeResultToXLSFile(prFlag=flag, prDefectId=defectId, prWb=wb, prWorkbookName='Classified_defects.xls')
