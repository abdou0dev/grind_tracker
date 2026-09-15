from tkinter import *
import gui, time, db_manager, saver, format_time, logging
logging.basicConfig(filename="logger.log", level=logging.DEBUG, format="%(asctime)s, %(message)s")

# NEXT: Context manager for other file's functions.

db_manager.init_db()
cursor = db_manager.get_connection()

today = time.strftime("%Y-%m-%d")
elapsed_seconds = 0
checkpoint = 0
timer_id = None

session_start_time = 0  # To save session time between starts and stops.
session_name = ""

def stopwatch():
	logging.info(f"stopwatch() started.")
	global elapsed_seconds, checkpoint, timer_id
	gui.time_label.config(text=format_time.format_time(time.time() - elapsed_seconds))
	logging.info(f"elapsed_seconds: {elapsed_seconds}")
	timer_id = gui.time_label.after(1000, stopwatch)


def start_timer():
	global elapsed_seconds, session_start_time, session_name
	gui.clear_info_label()
	session_name = gui.subject_entry.get()
	if not session_name:
		gui.info_label.config(text="Please provide a subject name first.", fg='red')
		return
	session_start_time = time.time()
	elapsed_seconds = time.time() - checkpoint
	logging.info(f"elapsed_seconds: {elapsed_seconds}, checkpoint: {checkpoint}")
	gui.start_button.config(state=DISABLED)
	gui.stop_button.config(state=ACTIVE)
	stopwatch()

def stop_timer():
	global timer_id, checkpoint, cursor, session_start_time
	checkpoint = time.time() - elapsed_seconds # To save elapsed time when stopping the timer.
	if timer_id:
		gui.time_label.after_cancel(timer_id)
		timer_id = None
	gui.stop_button.config(state=DISABLED)
	gui.start_button.config(state=ACTIVE) 
	# Save to DB.
	session_stop_time = time.time()
	duration_session_time = session_stop_time - session_start_time
	if duration_session_time > 60: # Only more than 1min long sessions will be saved.
		saver.save(today, session_start_time, session_stop_time, session_name, duration_session_time)
	else:
		gui.info_label.config(text="This session is not going to be saved\nbecause it is less than one minute long.", fg='red')



gui.start_button.config(command=start_timer)
gui.stop_button.config(command=stop_timer)
gui.window.mainloop()