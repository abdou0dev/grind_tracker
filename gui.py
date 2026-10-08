from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import db_utils, format_time
import logging

def clear_info_label():
	info_label.config(text="", fg='black')

def insert_treeview(data, tree):
	tree.delete(*tree.get_children()) # Clearing Treeview
	for session in data:
		tree.insert("", 'end', values=(session[0], session[1], format_time.format_duration(session[2]), format_time.format_time(session[3]), format_time.format_time(session[4])))
	

def search(search_type, keyword, tree):
	if search_type == 0:	# By date
		result = db_utils.search_by_date(keyword)
		logging.info(result)
	elif search_type == 1:	# By subject
		result = db_utils.search_by_subject(keyword)
	logging.info(f"original tree: {tree}")
	insert_treeview(result, tree)
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

	# Search Radiobuttons
	search_option = IntVar()
	Radiobutton(search_bar_frame,
		text='Date',
		variable=search_option,
		value=0,).pack(side='left')
	Radiobutton(search_bar_frame,
		text='Subject',
		variable=search_option,
		value=1).pack(side='left')

	# TreeView
	tree = ttk.Treeview(tree_frame,
		columns=("date", "subject", "duration", "start_time", "end_time"),
		show="headings")
	tree.heading("date", text="Date")
	tree.heading("subject", text="Subject")
	tree.heading("duration", text="Duration")
	tree.heading("start_time", text="Start Time")
	tree.heading("end_time", text="End Time")

	# Search Button
	search_button = Button(search_bar_frame,
		text="Search",
		font=('Arial', 10, 'bold'),
		command=lambda: search(search_option.get(), search_entry.get(), tree),
		)

	# Reset Button
	reset_button = Button(search_bar_frame,
		text="Reset",
		font=('Arial', 10, 'bold'),
		command=lambda: insert_treeview(db_utils.first_pull(), tree))
	reset_button.pack(side='right', padx=5)
	search_button.pack(side='right', padx=5)
	tree.pack()

	insert_treeview(db_utils.first_pull(), tree)

def summary():
	summary_win = Toplevel()
	summary_win.title("Summary")

	Label(summary_win,
		text="Summary",
		font=("Arial", 35, 'bold')
		).pack()
	# Frames.
	time_spent_frame = Frame(summary_win,)
	time_spent_frame.pack(fill='x', anchor='w')
	sessions_frame = Frame(summary_win,)
	sessions_frame.pack(fill='x', anchor='w')
	by_subject_frame = Frame(summary_win,)
	by_subject_frame.pack(fill='x', anchor='w')
	most_active_days_frame = Frame(summary_win,)
	most_active_days_frame.pack(fill='x', anchor='w')

	# TIME SPENT

	Label(time_spent_frame,
		text="Time Spent",
		font=("Arial", "20", 'bold'),
		pady=10).grid(row=0, column=0)

	# Today
	Label(time_spent_frame,
		text=f"Today",
		font=("Arial", 15)).grid(row=1, column=0, sticky=W)
	Label(time_spent_frame,
		text=f"{db_utils.time_spent_today()}",
		font=("Arial", 15)).grid(row=1, column=1, sticky=E)
	
	# This week
	Label(time_spent_frame,
		text=f"This week",
		font=("Arial", 15)).grid(row=2, column=0, sticky=W)
	Label(time_spent_frame,
		text=f"{db_utils.time_spent_week()}",
		font=("Arial", 15)).grid(row=2, column=1, sticky=E)

	# This month
	Label(time_spent_frame,
		text=f"This month",
		font=("Arial", 15)).grid(row=3, column=0, sticky=W)
	Label(time_spent_frame,
		text=f"{db_utils.time_spent_month()}",
		font=("Arial", 15)).grid(row=3, column=1, sticky=E)

	# All time
	Label(time_spent_frame,
		text=f"All time",
		font=("Arial", 15)).grid(row=4, column=0, sticky=W)
	Label(time_spent_frame,
		text=f"{db_utils.all_time()}",
		font=("Arial", 15)).grid(row=4, column=1, sticky=E)

	time_spent_frame.columnconfigure(1, weight=1)


	# SESSIONS

	Label(sessions_frame,
		text="Sessions",
		font=("Arial", "20", 'bold'),
		pady=10).grid(row=0, column=0)
	# Total
	Label(sessions_frame,
		text=f"Total",
		font=("Arial", 15)).grid(row=1, column=0, sticky=W)
	Label(sessions_frame,
		text=f"{db_utils.total_sessions()}",
		font=("Arial", 15)).grid(row=1, column=1, sticky=E)
	# Average
	Label(sessions_frame,
		text=f"Average",
		font=("Arial", 15)).grid(row=2, column=0, sticky=W)
	Label(sessions_frame,
		text=f"{db_utils.average_sessions_length()}",
		font=("Arial", 15)).grid(row=2, column=1, sticky=E)
	# Longest
	Label(sessions_frame,
		text=f"Longest",
		font=("Arial", 15)).grid(row=3, column=0, sticky=W)
	Label(sessions_frame,
		text=f"{db_utils.longest_session()}",
		font=("Arial", 15)).grid(row=3, column=1, sticky=E)

	sessions_frame.columnconfigure(1, weight=1)

	# By Subject
	Label(by_subject_frame,
		text="By Subject",
		font=("Arial", "20", 'bold'),
		pady=10).grid(row=0, column=0)

	row = 1
	for subject, duration in db_utils.subject_summary():
		Label(by_subject_frame,
		text=subject,
		font=("Arial", 15)).grid(row=row, column=0, sticky=W)
		Label(by_subject_frame,
		text=format_time.format_duration(duration),
		font=("Arial", 15)).grid(row=row, column=1, sticky=E)
		row+=1

	by_subject_frame.columnconfigure(1, weight=1)

	# Most Active Days

	Label(most_active_days_frame,
		text="Most Active Days",
		font=("Arial", "20", 'bold'),
		pady=10).grid(row=0, column=0)
	
	row = 1
	for day, duration in db_utils.most_active_days():
		Label(most_active_days_frame,
		text=day,
		font=("Arial", 15)).grid(row=row, column=0, sticky=W)
		Label(most_active_days_frame,
		text=format_time.format_duration(duration),
		font=("Arial", 15)).grid(row=row, column=1, sticky=E)
		row+=1

	most_active_days_frame.columnconfigure(1, weight=1)

def delete_history():
	confirmation = messagebox.askyesno(title="Delete History", message="Are you sure to delete your history?")
	if confirmation:
		backup = messagebox.askyesno(title='Backup', message="Do you want to save you history into a file and reset the program from zero?\n\nNO=Complete wipe of history.")
		db_utils.delete_history(backup)
		info_label.config(text="History has been deleted and a backup file has been saved.")

def custom_time_window():
	custom_win = Toplevel()
	custom_win.title("Set Custom Time")
	scale = Scale(custom_win,
		from_=1,
		to=60,
		orient=HORIZONTAL,
		length=400,
		font=("Arial", 15, 'bold'))
	scale.pack()

	Label(custom_win, text="Value is in Minutes.",
		font=("Arial", 15, 'bold'),
		).pack()
	result = {"minutes": 0}
	def submit():
		result["minutes"] = scale.get()
		custom_win.destroy()

	Button(custom_win,
		text="Submit",
		font=("Arial", 15, 'bold'),
		command=submit).pack()
	custom_win.grab_set()
	custom_win.wait_window()
	return result

def create_menubar(reset_timer, set_custom_time):
	# Menubar
	menubar = Menu(window)
	window.config(menu=menubar)
	# History Menu
	history_menu = Menu(menubar, tearoff=0)
	menubar.add_cascade(label="History", menu=history_menu)
	history_menu.add_command(label="View History", command=view_history)
	history_menu.add_command(label="Summary", command=summary)
	history_menu.add_separator()
	history_menu.add_command(label="Delete History", command=delete_history)

	# Action Menu
	action_menu = Menu(menubar, tearoff=0)
	menubar.add_cascade(label="Action", menu=action_menu)
	action_menu.add_command(label="Reset Timer", command=reset_timer)
	action_menu.add_command(label="Set Custom Time", command=set_custom_time)
	action_menu.add_separator()
	action_menu.add_command(label="Exit", command=quit)


window = Tk() # Instantiate an instance of a window.
window.title("Timer")


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