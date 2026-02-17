from pathlib import Path
import json
from plyer import notification

                # Function Method

File_Name = Path("/home/empire/Empire_DevOps/my_portfolio/todo_list.json")

def load_task():
    if File_Name.exists():
        try:
            with open(File_Name, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []  
    return []

def save_task(tasks):
    File_Name.parent.mkdir(parents=True, exist_ok=True)
    with open(File_Name, "w") as file:
        json.dump(tasks, file, indent=2)

def add_task(tasks):
    task = input("Enter task to add: ").capitalize()
    tasks.append(task)
    save_task(tasks)

    notification.notify(
        title="Task added",
        message= task,
        timeout= 5
    )

def remove_task(tasks):
    task = input("Enter task to remove: ").capitalize()
    if task in tasks:
        tasks.remove(task)
        print(f"{task} removed")
    else:
        print(f"{task} not found")

def view_task(tasks):
    if not tasks:
        print("No task available")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}- {task}")


def main():
    tasks = load_task()

    while True:
        print("\n1. Add task\n2. Remove task\n3. View task\n4. Quit or Exit")
        try:
            choice = int(input("choose between (1-4): "))
        except ValueError as e:
            print("Pleae enter a number")
            continue

        if choice == 1:
            add_task(tasks)
        if choice == 2:
            remove_task(tasks)
        if choice == 3:
            view_task(tasks)
        if choice == 4:
            break

main()
