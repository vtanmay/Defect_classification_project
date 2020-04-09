import CommonFunctionLibrary.CommonLibrary as cmnLib

# fetch defect data from JIRA - WB-2908, PLAT-216, WB-2806
projectId = 'WB'
defectId = 'WB-2806'
defectSummary = cmnLib.getDefectSummaryFromJira(prProject=projectId,prDefectId=defectId)
print("=== defect summary==",defectSummary)
#performanceKeywords =