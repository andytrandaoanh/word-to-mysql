import sys
import system_handler as sysHandle
from db_updater import upload_data


def prepareForUpload(pathIn, bookID):
	#print(pathIn)
	dbData = sysHandle.getListFromTextFile(pathIn)
	upload_data(bookID, dbData)
	#print(dbData)
	
	sys.exit()
