import json
from datetime import datetime

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        tasks = []
    return tasks

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task['title']} - {task['date']}")

def add_task(tasks, title):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    task = {"title": title, "date": date}
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")

def remove_task(tasks, task_index):
    try:
        removed_task = tasks.pop(task_index - 1)
        save_tasks(tasks)
        print(f"Task removed: {removed_task['title']}")
    except IndexError:
        print("Invalid task index. Please try again.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            title = input("Enter the task title: ")
            add_task(tasks, title)
        elif choice == '3':
            show_tasks(tasks)
            task_index = input("Enter the task index to remove: ")
            remove_task(tasks, int(task_index))
        elif choice == '4':
            print("Quitting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
