import time, logging
def format_time(epoch_time):
	logging.info(f"epoch_time: {epoch_time}")
	seconds = int(epoch_time % 60)
	minutes = int(epoch_time / 60) % 60
	hours = int(epoch_time / 3600)
	return f"{hours:02}:{minutes:02}:{seconds:02}"

def simple_time(epoch_time):
	if not epoch_time:
		return "--:--:--"
	try:
		epoch_time = float(epoch_time)
		time_structure = time.localtime(epoch_time)
		return time.strftime("%H:%M:%S", time_structure)
	except ValueError, OSError, OverflowError:
		return "Invalid"
