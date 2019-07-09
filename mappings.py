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

	mySql = ("INSERT INTO mappings "
	           "(word_form, sent_num, book_id)"
	           "VALUES (%s, %s, %s)")

	#print(mySql)
	cursor.execute(mySql, myData)
	db.commit()


def get_stop_words():
	DB_NAME = "lexicon"
	db = get_connection(DB_NAME)
	cursor = db.cursor()
	select_sql= ("select sword_form from stop_words order by 1;")
	try:
		cursor.execute(select_sql)
		records = cursor.fetchall()
		results = [item[0] for item in records]
		return results
	except Exception as e:
		print("Error encountered:", e)
	finally:
		cursor.close
		db.close



def upload_data(bookID, mapData):
	#print('bookID:', bookID)
	#print('mapData:', mapData)

	dataList = []
	for map in mapData:
		#prevent empty line
		if(map):
			line = map.split(',')
			tup = (line[0].replace("'", "''"), int(line[1]), bookID)
			dataList.append(tup)
	
	
	DB_NAME = "lexicon"

	db = get_connection(DB_NAME)

	cursor = db.cursor()
	for item in dataList:
		insert_row_to_database(item, cursor, db)
		print('uploading...', item)

	cursor.close()

	db.close()