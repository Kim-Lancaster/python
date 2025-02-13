# This is the first on the list of random projects that GTP suggests for begginer to intermediate programmers.
#Program will add a new task, view all tasks, mark a task as completed, and delete a task.
#You will also be able to add a due date and priority to each task.
#Task will persist even after the program is closed.

#Creating an empty list for our awesome task list.
import json
import os

#user_todo_list = []

def list_all_saved_todo_files():
    try:
        files = [f for f in os.listdir("lists") if f.endswith(".json")]
        if files:
            print("Previously saved To Do list.")
            for file in files:
                print(f"- {file[:-5]}")
        else:
            print("No previously saved To Do list saved.")
    except FileNotFoundError:
         print(f"The directory does not exist. No saved todo lists found.")

def save_to_file(file_name):
    os.makedirs("lists", exist_ok=True)
    with open(f"lists/{file_name}.json", "w") as file:
        json.dump(user_todo_list, file)

def load_from_file(file_name):
    global user_todo_list
    try:
        with open(f"lists/{file_name}.json", "r") as file:
            user_todo_list = json.load(file)
    except FileNotFoundError:
        print(f"No existing todo list with '{file_name}'. Starting with an empty list.")
        user_todo_list = []
    except json.JSONDecodeError:
        print(f"Error loading '{file_name}' todo list. Starting with an empty list.")
        user_todo_list = []
    


def add_task():
    while True:
        new_task = {
            "task" : input("New task: "),
            "due_date" : input("Due date (YYYY-MM-DD): "),
            "priority" : input("Priority (High/Medium/Low): "),
            "completed" : False
        }
        user_todo_list.append(new_task)
        add_another_task = input("Do you want to add another task (y/n): ")
        if add_another_task.lower() != 'y':
            break
    print("Task added successfully!")

def view_tasks():
    if not user_todo_list:
        print("No tasks to complete!")
    else:
        for index, tasks in enumerate(user_todo_list, 1):
            print(f"{index}. {tasks['task']}")
            print(f"Due date: {tasks['due_date']}")
            print(f"Priority: {tasks['priority']}")
            print(f"Completed: {tasks['completed']}\n")


def mark_task_completed():
    while True:
        view_tasks()
        selection = input("Enter the number of the task to mark as completed (press x to exit): ")
        if selection.lower() == 'x':
            break
        try:
            index = int(selection)
            if 1 <= index <= len(user_todo_list):
                task = user_todo_list[index - 1]
                task["completed"] = True
                print(f'{task["task"]} has been marked as completed.')
            else:
                print("Invalid selection!")
        except ValueError:
            print("Invalid selection!")
        continue_marking = input("Do you want to mark another task as completed (y/n): ")
        if continue_marking.lower()!= 'y':
            break

def delete_task():
    while True:
        view_tasks()
        selection = input("Enter the number of the task to delete (press x to exit): ")
        if selection.lower() == 'x':
            break
        try:
            index = int(selection)
            if 1 <= index <= len(user_todo_list):
                user_todo_list.pop(index - 1)
                print(f'{user_todo_list[index - 1]["task"]} has been deleted.')
            else:
                print("Invalid selection!")
        except ValueError:
            print("Invalid selection!")
        continue_delete = input("Do you want to delete another task (y/n): ")
        if continue_delete.lower()!= 'y':
            break
#The Welcome Screen
def welcome_screen():
    list_all_saved_todo_files()
    while True:
        filename = input("Enter your todo list file name (leave blank for default 'tasks'): ")
        #add fuction to list file names
        load_from_file(filename)
        while True:
            print("Welcome to your Todo List!")
            print("1. Add a new task")
            print("2. View all tasks")
            print("3. Mark a task as completed")
            print("4. Delete a task")
            print("5. Save and switch list")
            print("6. Exit")
            option = input("Enter your option: ")
            if option == "1":
                add_task()
            elif option == "2":
                view_tasks()
            elif option == "3":
                mark_task_completed()
            elif option == "4":
                delete_task()
            elif option == "5":
                saved_name = input("Save Todo list as: ")
                save_to_file(saved_name)
                print(f"Todo list '{filename}' saved.")
                break
            elif option == "6":
                print("Goodbye!")
            else:
                "Invalid option! Please try again."
        

welcome_screen()

