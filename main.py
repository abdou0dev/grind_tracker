from tkinter import *
import gui, time, db_manager, saver, format_time, logging
logging.basicConfig(filename="logger.log", level=logging.DEBUG, format="%(asctime)s, %(message)s")

# NEXT: Context manager for other file's functions.

#db_manager.init_db()

today = time.strftime("%Y-%m-%d")
elapsed_seconds = 0
checkpoint = 0
timer_id = None

def stopwatch():
	logging.info(f"stopwatch() started.")
	global elapsed_seconds, checkpoint, timer_id
	gui.time_label.config(text=format_time.format_time(time.time() - elapsed_seconds))
	logging.info(f"elapsed_seconds: {elapsed_seconds}")
	timer_id = gui.time_label.after(1000, stopwatch)


def start_timer():
	global elapsed_seconds
	elapsed_seconds = time.time() - checkpoint
	logging.info(f"elapsed_seconds: {elapsed_seconds}, checkpoint: {checkpoint}")
	gui.start_button.config(state=DISABLED)
	gui.stop_button.config(state=ACTIVE)
	stopwatch()

def stop_timer():
	global timer_id, checkpoint
	checkpoint = time.time() - elapsed_seconds # To save elapsed time when stopping the timer.
	if timer_id:
		gui.time_label.after_cancel(timer_id)
		timer_id = None
	gui.stop_button.config(state=DISABLED)
	gui.start_button.config(state=ACTIVE)



gui.start_button.config(command=start_timer)
gui.stop_button.config(command=stop_timer)
gui.window.mainloop()