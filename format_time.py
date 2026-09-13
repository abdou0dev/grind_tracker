def format_time(time):
	seconds = time % 60
	minutes = int(time / 60) % 60
	hours = int(time / 3600)
	return f"{hours:02}:{minutes:02}:{seconds:02}"
