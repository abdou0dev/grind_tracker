import sqlite3
import format_time

def init_db():
	# Connecting to db
	conn = sqlite3.connect("history.db")
	cursor = conn.cursor()

	# Defining session table
	cursor.execute("""CREATE TABLE IF NOT EXISTS sessions(
		id INTEGER PRIMARY KEY,
		date TEXT NOT NULL,
		subject TEXT,
		start_time REAL,
		end_time REAL,
		duration REAL) STRICT
	""")
	conn.commit()
	conn.close()

def get_connection():
	return sqlite3.connect("history.db")

def save_backup():
	table = str.maketrans({'-': '_'})
	today = format_time.today().translate(table)
	return sqlite3.connect(f"history_deleted_in{today}.db")