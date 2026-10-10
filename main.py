from tkinter import *
import gui, time, db_manager, saver, format_time, logging
logging.basicConfig(filename="logger.log", level=logging.DEBUG, format="%(asctime)s, %(message)s")

db_manager.init_db()
cursor = db_manager.get_connection()

today = time.strftime("%Y-%m-%d")
elapsed_seconds = 0
checkpoint = 0 # To save elapsed time when stopping the timer.
timer_id = None
custom_time = False

session_start_time = 0  # To save session time between starts and stops.
session_name = ""

def update_time_label(duration):
	gui.time_label.config(text=duration)

def stopwatch():
	global elapsed_seconds, timer_id
	update_time_label(format_time.format_duration(time.time() - elapsed_seconds))
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
	global timer_id, checkpoint, cursor, session_start_time, custom_time
	checkpoint = time.time() - elapsed_seconds
	if timer_id is None:
		return
	gui.time_label.after_cancel(timer_id)
	timer_id = None
	gui.stop_button.config(state=DISABLED)
	gui.start_button.config(state=ACTIVE) 
	# Save to DB.
	session_stop_time = time.time()
	if custom_time:
		session_time_duration = checkpoint
		session_start_time = session_stop_time - session_time_duration
		custom_time = False
	else:
		session_time_duration = session_stop_time - session_start_time
	logging.info(f"session_time_duration: {session_time_duration}")
	if session_time_duration > 60: # Only more than 1min long sessions will be saved.
		saver.save(today, session_start_time, session_stop_time, session_name, session_time_duration)
	else:
		gui.info_label.config(text="This session is not going to be saved\nbecause it is less than one minute long.", fg='red')

def reset_timer():
	global elapsed_seconds, checkpoint, timer_id, session_start_time, session_name
	stop_timer()
	elapsed_seconds = 0
	checkpoint = 0
	timer_id = None
	session_start_time = 0
	session_name = ""
	update_time_label(format_time.format_duration(elapsed_seconds))
	gui.stop_button.config(state=DISABLED)
	gui.start_button.config(state=ACTIVE)

def set_custom_time():
	global checkpoint, custom_time
	minutes = gui.custom_time_window()
	if minutes is None:
		return
	checkpoint = minutes * 60
	logging.info(f"checkpoint: {checkpoint}")
	update_time_label(format_time.format_duration(checkpoint))
	custom_time = True

gui.create_menubar(reset_timer, set_custom_time)
gui.start_button.config(command=start_timer)
gui.stop_button.config(command=stop_timer)
gui.window.mainloop()