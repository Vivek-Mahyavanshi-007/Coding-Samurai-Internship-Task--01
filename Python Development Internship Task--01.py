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
    
    