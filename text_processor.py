import sys
import system_handler as sysHandle
from db_updater import upload_data
import stop_words

def prepareForUpload(pathIn, bookID):
	#print(pathIn)
	dbData = sysHandle.getListFromTextFile(pathIn)
	upload_data(bookID, dbData)
	#print(dbData)
	
	sys.exit()


def uploadSpecialWords(pathIn):
	sWords = sysHandle.getListFromTextFile(pathIn)
	oldList = stop_words.get_stop_words()
	newList = [item for item in sWords if item not in oldList]
	if(newList):
		#print(newList)
		stop_words.upload_data(newList)
	else:
		print('nothing inserted, data already exists')