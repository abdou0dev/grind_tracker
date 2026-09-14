import time, db_manager, format_time

def save(today, start_time, end_time, duration):

	with db_manager.get_connection() as conn:
		conn.execute(
			"""INSERT INTO sessions
			(date, start_time, end_time, duration)
			VALUES (?,?,?,?)""",
			(today, start_time, end_time, duration)
		)
	return f"Session has been saved (duration: {format_time.format_time(duration)})"