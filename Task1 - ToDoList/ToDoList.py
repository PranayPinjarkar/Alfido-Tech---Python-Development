import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

class ToDoListApp:
  def __init__(self):
    self.root = tk.Tk()
    self.root.title("To-Do List")

    # Create the main frame
    self.main_frame = ttk.Frame(self.root)
    self.main_frame.pack(padx=10, pady=10)

    # Create the task list
    self.task_list = tk.Listbox(self.main_frame, font=("Times New Roman", 12), background="lightyellow", foreground="black")
    self.task_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create the buttons
    self.add_button = ttk.Button(self.main_frame, text="Add Task", command=self.add_task)
    self.add_button.pack(side=tk.TOP, pady=5)

    self.delete_button = ttk.Button(self.main_frame, text="Delete Task", command=self.delete_task)
    self.delete_button.pack(side=tk.TOP, pady=5)

    self.mark_done_button = ttk.Button(self.main_frame, text="Mark Done", command=self.mark_done_task)
    self.mark_done_button.pack(side=tk.TOP, pady=5)

    # Create the entry field for adding tasks
    self.task_entry = ttk.Entry(self.main_frame, font=("Times New Roman", 12),background="lightyellow", foreground="black")
    self.task_entry.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Create the calendar for selecting due dates
    self.cal = Calendar(self.main_frame, font=("Times New Roman", 10), selectmode="day")
    self.cal.pack_forget()

    # Create the button for selecting due date
    self.select_due_date_button = ttk.Button(self.main_frame, text="Select Due Date", command=self.show_calendar)
    self.select_due_date_button.pack(side=tk.TOP, pady=5)

    # Start the main loop
    self.root.mainloop()

  def add_task(self):
    task = self.task_entry.get()
    due_date = self.cal.selection_get()
    self.task_list.insert(tk.END, (task, due_date))
    self.task_entry.delete(0, tk.END)

  def delete_task(self):
    selected_item = self.task_list.curselection()
    if selected_item:
      self.task_list.delete(selected_item[0])

  def mark_done_task(self):
    selected_item = self.task_list.curselection()
    if selected_item:
      self.task_list.itemconfig(selected_item[0], foreground="red")

  def show_calendar(self):
    self.cal.pack(side=tk.TOP, pady=5)
    self.cal.bind("<<CalendarSelected>>", self.on_calendar_selected)

  def on_calendar_selected(self, event):
    due_date = self.cal.selection_get()
    selected_item = self.task_list.curselection()
    self.task_list.itemconfig(selected_item[0], values=(self.task_list.get(selected_item)[0], due_date))
    self.cal.pack_forget()

app = ToDoListApp()
