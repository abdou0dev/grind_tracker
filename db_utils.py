import sqlite3, db_manager, format_time, logging

cursor = db_manager.get_connection()
today = format_time.today()

def first_pull():
	global cursor

	db_data = cursor.execute("SELECT date, subject, duration, start_time, end_time FROM sessions").fetchall()
	return db_data

def search_by_date(keyword):
	return cursor.execute("SELECT date, subject, duration, start_time, end_time FROM sessions WHERE date LIKE ?", (f"%{keyword}%",)).fetchall()

def search_by_subject(keyword):
	return cursor.execute("SELECT date, subject, duration, start_time, end_time FROM sessions WHERE subject LIKE ?", (f"%{keyword}%",)).fetchall()

def time_spent_today():
	sessions = cursor.execute("SELECT duration FROM sessions WHERE date=?", (today,))
	total = 0
	for duration, in sessions:
		total+= duration
	return format_time.format_duration(total)

def time_spent_week():
	sessions = cursor.execute("SELECT duration FROM sessions WHERE date=?", (today,))