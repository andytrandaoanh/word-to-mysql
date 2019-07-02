#create table

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





def record_exists_in_database(myData, cursor, db):

	mySql = ("SELECT count(*) FROM words WHERE book_id = %s AND word_form LIKE %s;")

	
	cursor.execute(mySql, myData)

	word = cursor.fetchone()

	return bool(cursor.rowcount)

def insert_data_to_database(myData, cursor, db):

	mySql = ("INSERT INTO lexicon.words "
	           "(book_id, word_form, date_entered)"
	           "VALUES (%s, %s, NOW())")

	cursor.execute(mySql, myData)
	db.commit()


def safe_add_data(myData, cursor, db):


	if not record_exists_in_database(myData, cursor, db):
		insert_data_to_database(myData, cursor, db)
		#print('succeffuly inserted')




def upload_data(bookID, dbData):

	DB_NAME = "lexicon"

	db = get_connection(DB_NAME)

	cursor = db.cursor()
	for w in dbData:
		myData = (int(bookID), str(w))
		insert_data_to_database(myData, cursor, db)
		print('uploading...', myData)
		#safe_add_data(myData, cursor, db)

	cursor.close()

	db.close()

