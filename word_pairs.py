import os, sys
import mysql.connector
from mysql.connector import errorcode

def get_connection(dbname=''):
	try:
		connection = mysql.connector.connect(
		user='andyanh', password='DGandyanh#1234',
	    host='127.0.0.1', database = dbname)
		if connection.is_connected():
			return connection 
	except Error as e:
		return e




def insert_row_to_database(myData, cursor, db):

	mySql = ("INSERT INTO links "
	           "(dict_form, word_form)"
	           "VALUES (%s, %s)")

	try:
		cursor.execute(mySql, myData)
	except Exception as e:
		print("Error encountered:", e)
	
	db.commit()




def upload_data(dbData):
	
	#print(dataList)
	DB_NAME = "lexicon"

	db = get_connection(DB_NAME)

	cursor = db.cursor()
	for item in dbData:
		insert_row_to_database(item, cursor, db)
		print('uploading...', item)

	cursor.close()

	db.close()


	
def write_word_pairs(wordPairs):
	dbData = []
	for item in wordPairs:
		if(item):
			pair = item.split(',')
			tup = (pair[0].strip(), pair[1].strip())			
			dbData.append(tup)

	upload_data(dbData)