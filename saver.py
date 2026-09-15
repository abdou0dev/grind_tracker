import time, db_manager, format_time

def save(today, start_time, end_time, subject, duration):

	with db_manager.get_connection() as conn:
		conn.execute(
			"""INSERT INTO sessions
			(date, start_time, end_time, subject, duration)
			VALUES (?,?,?,?,?)""",
			(today, start_time, end_time, subject, duration)
		)
	return f"Session has been saved (duration: {format_time.format_time(duration)})"