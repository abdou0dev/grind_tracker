from tkinter import *
import time, db_manager, saver, format_time

# NEXT: Context manager for other file's functions.

db_manager.init_db()

today = time.strftime("%Y-%m-%d")
start_time = ""
elapsed_seconds = 0
timer_id = None

def stopwatch():
	global elapsed_seconds, timer_id
	time_label.config(text=format_time.format_time(elapsed_seconds))
	elapsed_seconds+=1
	timer_id = time_label.after(1000, stopwatch)

def start_timer():
	global start_time
	start_time = time.strftime("%H:%M:%S")
	start_button.config(state=DISABLED)
	stop_button.config(state=ACTIVE)
	stopwatch()

def stop_timer():
	global timer_id

	if timer_id:
		time_label.after_cancel(timer_id)
		timer_id = None
	stop_button.config(state=DISABLED)
	start_button.config(state=ACTIVE)

def saving():
	global today, start_time, elapsed_seconds
	stop_timer()
	info_label.config(text=saver.save(today, start_time, elapsed_seconds))

# GUI
window = Tk() # Instantiate an instance of a window.
window.title("Timer")

main_frame = Frame(window,)
main_frame.pack()
buttons_frame = Frame(window,)
buttons_frame.pack()
info_frame = Frame(window)
info_frame.pack()

# Time Label
time_label = Label(main_frame,
	text="00:00:00",
	foreground="green",
	font=('Arial', 100))
time_label.pack()

# Start button.
start_button = Button(buttons_frame,
	text="Start",
	command=start_timer,
	bg="green",
	foreground="white",
	width=15,
	height=1,
	font=("Arial", 20))
start_button.pack()

# Stop button
stop_button = Button(buttons_frame,
	text="Stop",
	command=stop_timer,
	bg="red",
	foreground="white",
	width=15,
	height=1,
	font=("Arial", 20))
stop_button.pack()

# save button
save_button = Button(buttons_frame,
	text="Save",
	command=saving,
	bg="blue",
	foreground="white",
	width=15,
	height=1,
	font=("Arial", 20))
save_button.pack()

# Info label
info_label = Label(info_frame,
	text="",
	foreground="black",
	font=('Arial', 20))
info_label.pack()

window.mainloop()