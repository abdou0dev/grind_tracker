from tkinter import *
from tkinter import ttk
import db_utils, format_time

def clear_info_label():
	info_label.config(text="", fg='black')

def view_history():
	history_window = Toplevel()
	history_window.title("History")

	# Search Bar Frame
	search_bar_frame = Frame(history_window,
		pady=5)
	search_bar_frame.pack()
	# Treeview Frame
	tree_frame = Frame(history_window,
		pady=5)
	tree_frame.pack()

	# Search Entry
	search_entry = Entry(search_bar_frame,
		font=("Arial", 10),
		width=50,
		)
	search_entry.pack(side="left", ipadx=5, ipady=1, padx=5)

	# Search Button
	search_button = Button(search_bar_frame,
		text="Search",
		font=('Arial', 10, 'bold'),
		)
	search_button.pack(side='right')

	tree = ttk.Treeview(tree_frame,
		columns=("date", "subject", "duration", "start_time", "end_time"),
		show="headings")
	tree.heading("date", text="Date")
	tree.heading("subject", text="Subject")
	tree.heading("duration", text="Duration")
	tree.heading("start_time", text="Start Time")
	tree.heading("end_time", text="End Time")
	tree.pack()

	data = db_utils.first_pull()
	print(data)
	for session in data:
		tree.insert("", 'end', values=(session[0], session[1], format_time.simple_time(session[2]), format_time.simple_time(session[3]), format_time.simple_time(session[4])))



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