import sqlite3

def init_db():
	# Connecting to db
	conn = sqlite3.connect("stopwatch.db")
	cursor = conn.cursor()

	# Defining session table
	cursor.execute("""CREATE TABLE IF NOT EXISTS sessions(
		id INTEGER PRIMARY KEY,
		date TEXT NOT NULL,
		start_time REAL,
		end_time REAL,
		duration REAL) STRICT
	""")
	conn.commit()
	conn.close()

def get_connection():
	return sqlite3.connect("stopwatch.db")