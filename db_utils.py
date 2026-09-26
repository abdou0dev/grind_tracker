import sqlite3, db_manager

cursor = db_manager.get_connection()

def first_pull():
	global cursor

	db_data = cursor.execute("SELECT date, subject, duration, start_time, end_time FROM sessions").fetchall()
	return db_data

def search_by_date(keyword):
	return cursor.execute("SELECT date, subject, duration, start_time, end_time FROM sessions WHERE date LIKE ?", (f"%{keyword}%",)).fetchall()

def search_by_subject(keyword):
	return cursor.execute("SELECT date, subject, duration, start_time, end_time FROM sessions WHERE subject LIKE ?", (f"%{keyword}%",)).fetchall()