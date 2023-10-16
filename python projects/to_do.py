# # A To-Do List application is a useful project that helps users manage
# # and organize their tasks efficiently. This project aims to create a
# # command-line or GUI-based application using Python, allowing
# # users to create, update, and track their to-do lists.
# # Initialize an empty list to store tasks
# # Initialize an empty list to store tasks
# tasks = []

# # Function to add a task
# def add_task():
#     title = input("Enter task title: ")
#     description = input("Enter task description: ")
#     task = {"title": title, "description": description, "completed": False}
#     tasks.append(task)
#     print("Task added successfully!")

# # Function to list all tasks
# def list_tasks():
#     for i, task in enumerate(tasks, start=1):
#         status = "Done" if task["completed"] else "Not Done"
#         print(f"{i}. Title: {task['title']}, Description: {task['description']}, Status: {status}")

# # Function to mark a task as completed
# def mark_completed():
#     list_tasks()
#     try:
#         task_number = int(input("Enter the task number to mark as completed: ")) - 1
#         if 0 <= task_number < len(tasks):
#             tasks[task_number]["completed"] = True
#             print("Task marked as completed!")
#         else:
#             print("Invalid task number.")
#     except ValueError:
#         print("Invalid input. Please enter a valid task number.")

# # Function to edit a task
# def edit_task():
#     list_tasks()
#     try:
#         task_number = int(input("Enter the task number to edit: ")) - 1
#         if 0 <= task_number < len(tasks):
#             title = input("Enter new task title: ")
#             description = input("Enter new task description: ")
#             tasks[task_number]["title"] = title
#             tasks[task_number]["description"] = description
#             print("Task edited successfully!")
#         else:
#             print("Invalid task number.")
#     except ValueError:
#         print("Invalid input. Please enter a valid task number.")

# # Main program loop
# while True:
#     print("\nOptions:")
#     print("1. Add Task")
#     print("2. List Tasks")
#     print("3. Mark Task as Completed")
#     print("4. Edit Task")
#     print("5. Quit")
    
#     choice = input("Enter your choice: ")
    
#     if choice == "1":
#         add_task()
#         add_more = input("Do you want to add more tasks? (yes/no): ").lower()
#         if add_more != "yes":
#             print("Thank you!")
#             break
#     elif choice == "2":
#         list_tasks()
#     elif choice == "3":
#         mark_completed()
#     elif choice == "4":
#         edit_task()
#     elif choice == "5":
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please select a valid option.")



#Task 1 Given by CodSoft
# python program to creat a todo list

import tkinter as tk
from tkinter import simpledialog, messagebox

def add_task():
    global listbox_tasks, entry_task
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    global listbox_tasks
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def edit_task():
    global listbox_tasks
    try:
        index = listbox_tasks.curselection()[0]
        old_task = listbox_tasks.get(index)
        new_task = simpledialog.askstring("Edit Task", "Edit the selected task:", initialvalue=old_task)
        if new_task:
            listbox_tasks.delete(index)
            listbox_tasks.insert(index, new_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to edit.")

def main():
    global listbox_tasks, entry_task
    root = tk.Tk()
    root.title("Task 1 To-Do List")

    frame_tasks = tk.Frame(root)
    frame_tasks.pack(pady=10)

    listbox_tasks = tk.Listbox(frame_tasks, width=50, height=10, selectbackground="green")
    listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

    scrollbar_tasks = tk.Scrollbar(frame_tasks)
    scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.BOTH)

    listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
    scrollbar_tasks.config(command=listbox_tasks.yview)

    entry_task = tk.Entry(root, width=50)
    entry_task.pack(pady=10)

    button_add_task = tk.Button(root, text="Add Task", command=add_task)
    button_add_task.pack(side=tk.LEFT, padx=5)

    button_delete_task = tk.Button(root, text="Delete Task", command=delete_task)
    button_delete_task.pack(side=tk.LEFT, padx=5)

    button_edit_task = tk.Button(root, text="Edit Task", command=edit_task)
    button_edit_task.pack(side=tk.LEFT, padx=5)

    root.mainloop()

if __name__ == "__main__":
    main()

