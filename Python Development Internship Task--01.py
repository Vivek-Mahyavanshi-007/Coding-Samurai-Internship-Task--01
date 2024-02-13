import colorama
import os
from colorama import Fore, Back, Style
import uuid

# Initialize colors
colorama.init(autoreset=True)

# Function to generate a unique ID for a task
def generate_unique_id(tasks):
    unique_id = str(uuid.uuid4())
    while unique_id in [task["id"] for task in tasks]:
        unique_id = str(uuid.uuid4())
    return unique_id

# Function to load tasks from a file
def load_tasks(filename):
    global tasks  # Declare tasks as global to modify it
    tasks = []  # Initialize empty task list
    if os.path.exists(filename):
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                task_data = line.strip().split(",")
                task = {
                    "id": task_data[0].split(":")[1].strip(),
                    "title": task_data[1].split(":")[1].strip(),
                    "description": task_data[2].split(":")[1].strip(),
                    "completed": True if task_data[3].split(":")[1].strip() == "True" else False
                }
                tasks.append(task)
        print(Fore.GREEN + f"Tasks loaded from '{filename}'.")
    else:
        print(Fore.YELLOW + f"File '{filename}' not found. Starting with an empty task list.")

# Function to save tasks to a file
def save_tasks(filename, tasks):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(f"ID: {task['id']},\n Title: {task['title']},\n Description: {task['description']},\n Completed: {task['completed']}\n")
    print(Fore.GREEN + f"Tasks saved to '{filename}'.")

# Function to add a task
def add_task(tasks):
    title = input(Fore.CYAN + "Enter Task Title: ")
    description = input(Fore.CYAN + "Enter Task Description: ")
    unique_id = generate_unique_id(tasks)
    tasks.append({"title": title, "description": description, "id": unique_id, "completed": False})
    print(Fore.GREEN + "Task Added Successfully!")

# Function to list all tasks
def list_tasks(tasks):
    if not tasks:
        print(Fore.YELLOW + "No Tasks Found!")
    else:
        for task in tasks:
            status = "Completed" if task["completed"] else "Incomplete"
            print(
                f"{Fore.MAGENTA}ID: {task['id']}{Fore.WHITE},\n {Fore.CYAN}Title: {task['title']}{Fore.WHITE},\n {Fore.YELLOW}Description: {task['description']}{Fore.WHITE},\n {Fore.GREEN}Status: {status}"
            )

# Function to mark a task as complete
def mark_complete(tasks):
    task_id = input(Fore.YELLOW + "Enter Task ID to Mark Complete: ")
    found = False
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            found = True
            print(Fore.GREEN + "Task Marked Completed!")
            break
    if not found:
        print(Fore.RED + "Task ID Not Found!")

# Function to delete a task
def delete_task(tasks):
    task_id = input(Fore.RED + "Enter Task ID To Delete: ")
    found = False
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            del tasks[i]
            found = True
            print(Fore.GREEN + "Task Deleted Successfully!")
            break
    if not found:
        print(Fore.RED + "Task ID Not Found!")

# Main function to run the application
def main():
    tasks = []  # Initialize empty task list
    filename = "Output_Tasks.txt"  # Change the filename here
    load_tasks(filename)

    while True:
        print(Fore.LIGHTGREEN_EX + "\nTask Manager")
        print(Fore.CYAN + "-" * 50)
        print(Fore.WHITE + "\n1. Add Task")
        print(Fore.WHITE + "2. List Tasks")
        print(Fore.YELLOW + "3. Load Tasks (from different file)")
        print(Fore.YELLOW + "4. Mark Task as Complete")
        print(Fore.RED + "5. Delete Task")
        print(Fore.GREEN + "6. Save Tasks")
        print(Fore.MAGENTA + "7. Exit")
        print(f"Current file: {filename}")
        print(Fore.CYAN + "._." * 50)

        # Get user choice with error handling
        try:
            choice = input(Fore.CYAN + "\n Enter your choice: ")
            int_choice = int(choice)
        except ValueError:
            print(Fore.RED + "Invalid choice. Please enter a number between 1 and 7.")
            continue

        # Handle user choices with respective functions
        if int_choice == 1:
            add_task(tasks)
        elif int_choice == 2:
            list_tasks(tasks)
        elif int_choice == 3:
            new_filename = input(Fore.CYAN + "Enter new filename to load tasks: ")
            if os.path.exists(new_filename):
                load_tasks(new_filename)
                filename = new_filename
                print(Fore.GREEN + f"Tasks loaded from '{filename}'.")
            else:
                print(Fore.YELLOW + f"File '{new_filename}' not found.")
        elif int_choice == 4:
            mark_complete(tasks)
        elif int_choice == 5:
            delete_task(tasks)
        elif int_choice == 6:
            save_tasks(filename, tasks)
        elif int_choice == 7:
            save_tasks(filename, tasks)
            print(Fore.GREEN + "Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
