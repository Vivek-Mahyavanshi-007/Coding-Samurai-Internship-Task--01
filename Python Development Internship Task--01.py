import os
from colorama import init, Fore, Back, Style
import uuid

init(autoreset=True)

# Function to add a task
def add_task(tasks):
    print(Back.GREEN + Fore.WHITE + "Add Task")
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    unique_id = generate_unique_id(tasks)
    tasks.append({"title": title, "description": description, "id": unique_id, "completed": False})
    print(Style.RESET_ALL + Fore.GREEN + "Task added successfully!")
    
# Function to list all tasks
def list_tasks(tasks):
    print(Back.BLUE + Fore.WHITE + "List Tasks")
    if not tasks:
        print("No tasks found!")
    else:
        for task in tasks:
            status = "Completed" if task["completed"] else "Incomplete"
            print(f"ID: {task['id']}, Title: {task['title']}, Description: {task['description']}, Status: {status}")
    print(Style.RESET_ALL)

# Function to mark a task as complete
def mark_complete(tasks):
    print(Back.YELLOW + Fore.WHITE + "Mark Task as Complete")
    task_id = input("Enter task ID to mark complete: ")
    found = False
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            found = True
            print(Fore.YELLOW + "Task marked completed!")
            break
    if not found:
        print(Fore.RED + "Task ID not found!")
    print(Style.RESET_ALL)
