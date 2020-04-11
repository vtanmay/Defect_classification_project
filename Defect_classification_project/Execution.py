import CommonFunctionLibrary.CommonLibrary as cmnLib

# fetch defect data from JIRA - WB-2908-P, WB-2806-P, WB-3202-NP
projectId = 'WB'
defectId = 'WB-2908'
defectSummary = cmnLib.getDefectSummaryFromJira(prProject=projectId, prDefectId=defectId)
#print("=== defect summary==",defectSummary)
# read performance keywords data from excel
loc = (cmnLib.getCurrentWorkingDirecotry()+"\Reference_keywords.xlsx")
listOfPerfKeywords = cmnLib.getPerformanceKeywordsFromExcelSheet(prFilePath=loc, prSheetName='Performance Keywords')
#print("==== perf keywords from sheet ===", listOfPerfKeywords)
wb = cmnLib.createXLSFileAndReturnXLSWb(prWorkbookName='Classified_defects.xls', prWorkbookSheet='classified defects')
cmnLib.classifyDefect(prDefectId=defectId, prDefDetailsList=defectSummary, prRefKwList=listOfPerfKeywords, prWb=wb, prWorkbookName='Classified_defects.xls')
