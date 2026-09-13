from tkinter import *

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
	bg="green",
	foreground="white",
	width=15,
	height=1,
	font=("Arial", 20))
start_button.pack()

# Stop button
stop_button = Button(buttons_frame,
	text="Stop",
	bg="red",
	foreground="white",
	width=15,
	height=1,
	font=("Arial", 20))
stop_button.pack()

# save button
save_button = Button(buttons_frame,
	text="Save",
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