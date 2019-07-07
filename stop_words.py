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

	mySql = ("INSERT INTO lexicon.stop_words "
	           "(sword_form, date_entered)"
	           "VALUES ('" + myData + "', NOW())")

	#print(mySql)
	cursor.execute(mySql)
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

def fixQuote(sInput):
	try:
		strTemp = str(sInput)
		sOutput = strTemp.replace("'", "''")
		return sOutput
	except Exception as e:
		print(e) 


def upload_data(dbData):

	DB_NAME = "lexicon"

	db = get_connection(DB_NAME)

	cursor = db.cursor()
	for w in dbData:
		if (w):
			myData = (fixQuote(w))
			insert_row_to_database(myData, cursor, db)
			print('uploading...', myData)

	cursor.close()

	db.close()