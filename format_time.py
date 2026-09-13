import time, logging
def format_time(epoch_time):
	logging.info(f"epoch_time: {epoch_time}")
	seconds = int(epoch_time % 60)
	minutes = int(epoch_time / 60) % 60
	hours = int(epoch_time / 3600)
	return f"{hours:02}:{minutes:02}:{seconds:02}"