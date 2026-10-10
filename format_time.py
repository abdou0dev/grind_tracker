import time, logging
from datetime import date, timedelta
from calendar import monthrange

def today():
	return time.strftime("%Y-%m-%d")

def format_duration(epoch_time):
	if epoch_time is None:
		return "00:00:00"
	else:
		seconds = int(epoch_time % 60)
		minutes = int(epoch_time / 60) % 60
		hours = int(epoch_time / 3600)
		return f"{hours:02}:{minutes:02}:{seconds:02}"

def format_time(epoch_time):
	if not epoch_time:
		return "--:--:--"
	try:
		epoch_time = float(epoch_time)
		time_structure = time.localtime(epoch_time)
		return time.strftime("%H:%M:%S", time_structure)
	except ValueError, OSError, OverflowError:
		return "Invalid"

def this_week():
	today = date.today()
	monday = today - timedelta(days=today.weekday())
	sunday = monday + timedelta(days=6)

	return (monday.isoformat(), sunday.isoformat())

def this_month():
	today = date.today()
	first_day = today.replace(day=1)
	last_day = today.replace(day=monthrange(today.year, today.month)[1])
	logging.info(f"FIRST DAY: {first_day}, LAST DAY: {last_day}")
	return (first_day, last_day)
