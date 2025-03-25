import json
import hashlib

# File paths for storing user data and tasks
USER_DATA_FILE = 'users.json'
TASKS_DATA_FILE = 'tasks.json'

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to load user data from file
def load_users():
    try:
        with open(USER_DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save user data to file
def save_users(users):
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(users, file)

# Function to load tasks from file
def load_tasks():
    try:
        with open(TASKS_DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save tasks to file
def save_tasks(tasks):
    with open(TASKS_DATA_FILE, 'w') as file:
        json.dump(tasks, file)

# User Registration
def register():
    users = load_users()
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists. Please choose a different username.")
        return
    password = input("Enter a password: ")
    users[username] = hash_password(password)
    save_users(users)
    print("Registration successful!")

# User Login
def login():
    users = load_users()
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username] == hash_password(password):
        print("Login successful!")
        return username
    else:
        print("Invalid username or password.")
        return None

# Add a Task
def add_task(username):
    tasks = load_tasks()
    if username not in tasks:
        tasks[username] = []
    task_description = input("Enter task description: ")
    task_id = len(tasks[username]) + 1
    tasks[username].append({"id": task_id, "description": task_description, "status": "Pending"})
    save_tasks(tasks)
    print("Task added successfully!")

# View Tasks
def view_tasks(username):
    tasks = load_tasks()
    if username in tasks and tasks[username]:
        print("Your Tasks:")
        for task in tasks[username]:
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")
    else:
        print("No tasks found.")

# Mark a Task as Completed
def mark_task_completed(username):
    tasks = load_tasks()
    if username in tasks and tasks[username]:
        task_id = int(input("Enter task ID to mark as completed: "))
        for task in tasks[username]:
            if task['id'] == task_id:
                task['status'] = 'Completed'
                save_tasks(tasks)
                print("Task marked as completed.")
                return
        print("Task ID not found.")
    else:
        print("No tasks found.")

# Delete a Task
def delete_task(username):
    tasks = load_tasks()
    if username in tasks and tasks[username]:
        task_id = int(input("Enter task ID to delete: "))
        tasks[username] = [task for task in tasks[username] if task['id'] != task_id]
        save_tasks(tasks)
        print("Task deleted successfully.")
    else:
        print("No tasks found.")


def menu(username):
    while True:
        print("\nMenu:")
        print("1. Add a Task")
        print("2. View Tasks")
        print("3. Mark a Task as Completed")
        print("4. Delete a Task")
        print("5. Logout")
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_task(username)
        elif choice == '2':
            view_tasks(username)
        elif choice == '3':
            mark_task_completed(username)
        elif choice == '4':
            delete_task(username)
        elif choice == '5':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

# Main Function
def main():
    while True:
        print("\nWelcome to Task Manager")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            register()
        elif choice == '2':
            username = login()
            if username:
                menu(username)
        elif choice == '3':
            print("Exiting the application. Goodbye!")
            break
        else:
            return
        
if __name__ == "__main__":
    main()
           