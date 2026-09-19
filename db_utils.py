import sqlite3, db_manager

cursor = db_manager.get_connection()

def first_pull():
	global cursor

	db_data = cursor.execute("SELECT date, subject, duration, start_time, end_time FROM sessions").fetchall()
	return db_data
		