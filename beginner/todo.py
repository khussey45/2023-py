# Modules 
import time 

# Create an empty to-do list
todo_list = []

# Function to add a task to the to-do list
def add_task(task):
    todo_list.append(task)
    print("Task added: ", task)

# Function to remove a task from the to-do list
def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print("Task removed: ", task)
    else:
        print("Task not found in the to-do list.")

# Function to display the current to-do list
def display_tasks():
    print("To-Do List:")
    if len(todo_list) == 0:
        print("No tasks.")
    else:
        for task in todo_list:
            print("-", task)

# Main program loop
while True:
    print("\n===== To-Do List Manager =====")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Display Tasks")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == "2":
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == "3":
        display_tasks()
        time.sleep(2)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
