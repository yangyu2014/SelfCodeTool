#!/usr/bin/python
#coding:utf-8
import os,shutil,re,xlrd,sys,json
reload(sys)
sys.setdefaultencoding("utf-8")

class FileTools(object):
	@classmethod
	def GoToCurrentFilePosition(cls):
		dirPath = FileTools.GetCurrentFilePosition()
		os.chdir(dirPath)

 	@classmethod
	def GetCurrentFilePosition(cls):     		
		path = sys.path[0]
		if os.path.isdir(path):
			return path
		elif os.path.isfile(path):
			return os.path.dirname(path)

  	@classmethod
	def ReCreateTargetDir(cls,TargetDir):
		if os.path.isdir(TargetDir):
			shutil.rmtree(TargetDir)
		os.mkdir(TargetDir)

	@classmethod
	def WriteStringToFile(cls,FileFullPath,ContentString):
		fileWrite = open(FileFullPath,"w")
		try:
			fileWrite.write(ContentString)
		finally:
			print "Finish write : < " + FileFullPath + " >!!!"
			fileWrite.close()

	@classmethod
	def WriteJsonToFile(cls,FileFullPath,ContentDicOrArray):
		FileTools.WriteStringToFile(FileFullPath,json.dumps(ContentDicOrArray,ensure_ascii=True,sort_keys=True,indent=2))

	@classmethod
	def ReadStringFromFile(cls,FileFullPath):
		fileRead = open(FileFullPath)
		try:
			txt = fileRead.read()
		finally:
			fileRead.close
		return txt
		
	@classmethod
	def ReadXlsxToDic(cls, XlsxFileDirPath, XlsxName):
		XlsxFileFullPath = XlsxFileDirPath + XlsxName
		if os.path.isfile(XlsxFileFullPath) and XlsxName != ".DS_Store":
			excelFile = xlrd.open_workbook(XlsxFileFullPath)
			sheetTables = {}
			for sheetIndex in range(excelFile.nsheets):
				sheet = excelFile.sheet_by_index(sheetIndex)
				sheetName = excelFile.sheet_names()[sheetIndex]
				lang_keys = []
				rowTables = {}
				for rowIndex in range(sheet.nrows):	
					rowData = {}
					rowName = ""
					for colIndex in range(sheet.ncols):
						if(rowIndex == 0):
							lang_keys.append(sheet.cell_value(rowx=rowIndex, colx=colIndex))
						else:
							rowData[lang_keys[colIndex]] = sheet.cell_value(rowx=rowIndex, colx=colIndex)
					if (rowIndex != 0):
						lang_content = rowData[lang_keys[0]]
						rowTables[lang_content] = rowData
				sheetTables[sheetName] = rowTables
			return sheetTables
		else:
			return {}