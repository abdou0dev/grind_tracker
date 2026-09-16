from tkinter import *
import db_utils

def clear_info_label():
	info_label.config(text="", fg='black')

def view_history():
	history_window = Toplevel()
	history_window.title("History")

	search_entry = Entry(history_window,
		font=("Arial", 10),
		width=50,
		)
	search_entry.pack(side="left", ipadx=5, ipady=1, padx=5)

	search_button = Button(history_window,
		text="Search",
		font=('Arial', 10, 'bold'),
		)
	search_button.pack(side='right')


window = Tk() # Instantiate an instance of a window.
window.title("Timer")

# Menubar
menubar = Menu(window)
window.config(menu=menubar)
# History Menu
history_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="History", menu=history_menu)
history_menu.add_command(label="View History", command=view_history)
history_menu.add_command(label="Summary")
history_menu.add_separator()
history_menu.add_command(label="Delete History")

# Action Menu
action_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Action", menu=action_menu)
action_menu.add_command(label="Reset Timer")
action_menu.add_command(label="Set Custom Time")
action_menu.add_separator()
action_menu.add_command(label="Exit", command=quit)


# Frames
top_frame = Frame(window,)
top_frame.pack()
main_frame = Frame(window,)
main_frame.pack()
buttons_frame = Frame(window,)
buttons_frame.pack()
info_frame = Frame(window)
info_frame.pack()

# Subject Entry
subject_entry = Entry(top_frame,
	font=('Arial', 15),
	width=30,
	)
subject_entry.pack(side='right', padx=5, ipadx=5, ipady=2)

# Subject label
subject_label = Label(top_frame,
	text="session's subject",
	font=('Arial', 15),
	)
subject_label.pack(side='left', padx=5)
# Time Label
time_label = Label(main_frame,
	text="00:00:00",
	foreground="green",
	font=('Arial', 100),
	)
time_label.pack()

# Start button.
start_button = Button(buttons_frame,
	text="Start",
	bg="green",
	foreground="white",
	width=15,
	height=1,
	font=("Arial", 20),
	)
start_button.pack(side='left', padx=10)

# Stop button
stop_button = Button(buttons_frame,
	text="Stop",
	bg="red",
	foreground="white",
	width=15,
	height=1,
	font=("Arial", 20),
	)
stop_button.pack(side='right', padx=10)

# Info label
info_label = Label(info_frame,
	text="",
	foreground="black",
	font=('Arial', 20),
	)
info_label.pack()

stop_button.config(state=DISABLED)