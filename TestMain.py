#!/usr/bin/python
from Tools import *
TestFlag = "Test_FileTools"
if __name__ == "__main__":
	if TestFlag == "Test_ReadXlsx":
		pass
	elif TestFlag == "Test_FileTools":
		FileTools.GoToCurrentFilePosition()
		FileTools.ReCreateTargetDir(FileTools.GetCurrentFilePosition() + "/Output/")
		FileTools.WriteStringToFile(FileTools.GetCurrentFilePosition() + "/Output/haha.json","shatuotuo shatuotuo shatuotuo")
		aa = []
		aa.append(FileTools.ReadStringFromFile(FileTools.GetCurrentFilePosition() + "/Output/haha.json"))
		print aa
		FileTools.WriteJsonToFile(FileTools.GetCurrentFilePosition() + "/Output/haha.json",aa)

	else:
		print "==============>TestFlag : " + TestFlag
