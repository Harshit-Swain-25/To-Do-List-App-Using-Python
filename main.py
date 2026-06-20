import json
import os

FILE = "tasks.json"

def load_tasks():
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def next_id(tasks):
    if not tasks:
        return 1
    return max(t["id"] for t in tasks) + 1

def list_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for t in tasks:
        status = "✓" if t.get("done") else " "
        print(f"[{status}] {t['id']}: {t['task']}")

def add_task(tasks, text):
    tasks.append({"id": next_id(tasks), "task": text, "done": False})
    save_tasks(tasks)
    print("Task added.")

def mark_done(tasks, id_):
    for t in tasks:
        if t["id"] == id_:
            t["done"] = True
            save_tasks(tasks)
            print("Task marked done.")
            return
    print("Task id not found.")

def remove_task(tasks, id_):
    for i, t in enumerate(tasks):
        if t["id"] == id_:
            tasks.pop(i)
            save_tasks(tasks)
            print("Task removed.")
            return
    print("Task id not found.")

def main():
    tasks = load_tasks()
    menu = """
To-Do List
1) List tasks
2) Add task
3) Mark task as done
4) Remove task
5) Exit
"""
    while True:
        print(menu)
        choice = input("Choose (1-5): ").strip()
        if choice == '1':
            list_tasks(tasks)
        elif choice == '2':
            text = input("Task description: ").strip()
            if text:
                add_task(tasks, text)
            else:
                print("Empty task not added.")
        elif choice == '3':
            try:
                id_ = int(input("Enter task id to mark done: "))
                mark_done(tasks, id_)
            except ValueError:
                print("Enter a numeric id.")
        elif choice == '4':
            try:
                id_ = int(input("Enter task id to remove: "))
                remove_task(tasks, id_)
            except ValueError:
                print("Enter a numeric id.")
        elif choice == '5':
            print("Bye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
