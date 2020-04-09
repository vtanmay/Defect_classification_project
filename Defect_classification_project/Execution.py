import CommonFunctionLibrary.CommonLibrary as cmnLib

# fetch defect data from JIRA - WB-2908, WB-2806-P, WB-3202-NP
projectId = 'WB'
defectId = 'WB-2806'
defectSummary = cmnLib.getDefectSummaryFromJira(prProject=projectId, prDefectId=defectId)
#print("=== defect summary==",defectSummary)
# read performance keywords data from excel
loc = (cmnLib.getCurrentWorkingDirecotry()+"\Reference_keywords.xlsx")
listOfPerfKeywords = cmnLib.getPerformanceKeywordsFromExcelSheet(prFilePath=loc, prSheetName='Performance Keywords')
#print("==== perf keywords from sheet ===", listOfPerfKeywords)
cmnLib.classifyDefect(prDefDetailsList=defectSummary, prRefKwList=listOfPerfKeywords)