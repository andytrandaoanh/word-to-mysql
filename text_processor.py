import sys
import system_handler as sysHandle
from db_updater import upload_data
import stop_words, mappings, word_pairs

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
	sys.exit()

def uploadMappings(pathIn):
	bookID = sysHandle.getBookIDFromMapFileName(pathIn)
	#print('bookID:', bookID)
	mapList = sysHandle.getListFromTextFile(pathIn)
	mappings.upload_data(bookID, mapList)
	sys.exit()	

def uploadWordPairs(pathIn):
	wordPairList = sysHandle.getListFromTextFile(pathIn)
	word_pairs.write_word_pairs(wordPairList)
	#print('pathIn', pathIn)	