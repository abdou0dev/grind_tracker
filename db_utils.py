import sqlite3, db_manager, format_time, logging

cursor = db_manager.get_connection()


def first_pull():
	global cursor

	db_data = cursor.execute("SELECT date, subject, duration, start_time, end_time FROM sessions").fetchall()
	return db_data

def search_by_date(keyword):
	return cursor.execute("SELECT date, subject, duration, start_time, end_time FROM sessions WHERE date LIKE ?", (f"%{keyword}%",)).fetchall()

def search_by_subject(keyword):
	return cursor.execute("SELECT date, subject, duration, start_time, end_time FROM sessions WHERE subject LIKE ?", (f"%{keyword}%",)).fetchall()

def time_spent_today():
	today = format_time.today()
	duration_total = cursor.execute("SELECT SUM(duration) FROM sessions WHERE date=?", (today,)).fetchone()
	return format_time.format_duration(duration_total[0])

def time_spent_week():
	duration_total = cursor.execute("SELECT SUM(duration) FROM sessions WHERE date BETWEEN ? AND ?", format_time.this_week()).fetchone()
	return format_time.format_duration(duration_total[0])

def time_spent_month():
	duration_total = cursor.execute("SELECT SUM(duration) FROM sessions WHERE date BETWEEN ? AND ?", format_time.this_month()).fetchone()
	return format_time.format_duration(duration_total[0])

def all_time():
	duration_total = cursor.execute("SELECT SUM(duration) FROM sessions").fetchone()
	return format_time.format_duration(duration_total[0])

def total_sessions():
	total_sessions = cursor.execute("SELECT id FROM sessions").fetchall()
	return len(total_sessions)

def average_sessions_length():
	average_length = cursor.execute("SELECT AVG(duration) FROM sessions").fetchone()
	return format_time.format_duration(average_length[0])

def longest_session():
	longest_duration = cursor.execute("SELECT MAX(duration) FROM sessions").fetchone()
	return format_time.format_duration(longest_duration[0])

def subject_summary():	
	result = cursor.execute("""SELECT subject, SUM(duration)
		FROM sessions
		GROUP BY subject
		ORDER BY SUM(duration) DESC""")
	return result

def most_active_days():
	result = cursor.execute("""SELECT date, SUM(duration)
		FROM sessions
		GROUP BY date
		ORDER BY SUM(duration) DESC
		LIMIT 3""")
	return result