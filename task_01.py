import customtkinter
import tkinter as tk
from tkinter import ttk
import json
import os

root = customtkinter.CTk()
root.geometry("500x550")
root.title("TO-DO")

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

todo_list = 'tasks.json'


def load_tasks():
  if os.path.exists(todo_list):
        with open(todo_list, "r") as file:
            try:
                data = json.load(file)
                if isinstance(data, list):
                    for task in data:
                        if 'completed' not in task:
                            task['completed'] = False
                    return data
                else:
                    print("No Data")
                    return []
            except json.JSONDecodeError:
                print("Error decoding JSON")
                return []
        return []

def save_task():

    with open(todo_list, "w") as file:
        json.dump(tasks, file)

tasks = load_tasks()

def add_task():

    task_val = taskbox.get()

    if task_val:
        tasklist.insert('', 'end', values=(task_val,))
        tasks.append({'task': task_val,'completed': False})
        save_task()
        taskbox.delete(0, tk.END)

def remove_task():
    selected_items = tasklist.selection() 

    if selected_items:
        for item in selected_items:
            values = tasklist.item(item, 'values')
            
            tasks[:] = [task for task in tasks if task['task'] != values[0]]
            tasklist.delete(item)
        
        save_task() 

def edit_task():
    selected_item = tasklist.selection()

    if selected_item:
        item = tasklist.item(selected_item)
        values = item['values']

        tasks.delete(0, 'end')
        tasks.insert(0, values[0])

        tasks[:] = [task for task in tasks if task['task'] != values[0]]
        tasklist.delete(item)
        
    save_task() 


def complete_task():
    selected_items = tasklist.selection()
    if selected_items:
        for item in selected_items:
            values = tasklist.item(item, 'values')
            for task in tasks:
                if task['task'] == values[0]:
                    task['completed'] = True
                    tasklist.delete(item)
                    completetasklist.insert('', 'end', values=(task['task'],))
        save_task()


def display_tasks():
   for task in tasks:
        if task['completed']:
            completetasklist.insert("", "end", values=(task["task"],))
        else:
            tasklist.insert("", "end", values=(task["task"],))

taskbox = customtkinter.CTkEntry(root, placeholder_text= "Add task", width=495, height= 50)
taskbox.pack(pady = 20)

addbtn = customtkinter.CTkButton(root, text="Add Task", command= add_task)
addbtn.pack(pady = 10)

tabview = customtkinter.CTkTabview(master=root,width= 495, bg_color="transparent")
tabview.pack(padx=5, pady=10)

tabview.add("Incomplete")  
tabview.add("Complete")  
tabview.set("Incomplete") 



tasklist = ttk.Treeview(tabview.tab("Incomplete"), columns = ('task'), show= "headings")
tasklist.heading('task', text="Tasks")
tasklist.pack(pady= 10, padx=5, fill='both')

btnframe = customtkinter.CTkFrame(tabview.tab("Incomplete"))
btnframe.pack(pady=10)

deletebtn = customtkinter.CTkButton(btnframe, text="Remove Task", command=remove_task)
deletebtn.grid(row=0, column=1, padx=5)

completebtn = customtkinter.CTkButton(btnframe, text="Complete Task", command= complete_task)
completebtn.grid(row=0, column=2, padx=5)


#completed tasks

completetasklist = ttk.Treeview(tabview.tab("Complete"), columns = ('task'), show= "headings")
completetasklist.heading('task', text="Tasks")
completetasklist.pack(pady= 10, padx=5, fill='both')



display_tasks()

root.mainloop()