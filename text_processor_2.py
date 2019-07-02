import os, sys
import system_handler as sysHandle
from mysql_data import getWordList


def convertList(rawList):
	arr = rawList.split('\n')
	return arr


def filterList(rawList, dictList):

	listClear = [item for item in rawList if item.lower() in dictList]
	listTrash =  [item for item in rawList if item not in listClear]
	return(listClear, listTrash)

def splitDictByCase(list1):

	list2 = list(filter(lambda s: s.islower(), list1))
	list3 =  [item for item in list1 if item not in list2]
	return(list2, list3)	

def processText(inFile, outDir, dbDir):
	pathRecycleOut = sysHandle.getRawPath(inFile, outDir)
	pathDatabaseIn = sysHandle.getRawPath(inFile, dbDir)
	trashListIn = sysHandle.getWordFromTextFile(inFile)
	databseListIn = sysHandle.getWordFromTextFile(pathDatabaseIn)
	recycleListOut = [item for item in trashListIn if item not in databseListIn]
	standardList = getWordList()
	newRecycle = [item for item in recycleListOut if item not in standardList]
	#print (newRecycle)

	sysHandle.writeListToFile(newRecycle, pathRecycleOut)
	sysHandle.openDir(outDir)
	sys.exit()

