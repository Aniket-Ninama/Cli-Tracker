import json
import argparse
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(description):
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "description": description,
        "status": "todo"
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task added: {description}")

def update_task(task_id, description=None, status=None):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            if description:
                task["description"] = description
            if status:
                task["status"] = status
            save_tasks(tasks)
            print(f"🔄 Task {task_id} updated.")
            return
    print(f"❌ Task with ID {task_id} not found.")

def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]
    if len(new_tasks) != len(tasks):
        save_tasks(new_tasks)
        print(f"🗑️ Task {task_id} deleted.")
    else:
        print(f"❌ Task with ID {task_id} not found.")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.")
        return
    for task in tasks:
        print(f"[{task['id']}] ({task['status']}) - {task['description']}")

def tasks_status(status):
    tasks = load_tasks()
    for task in tasks:
        if task["status"] == status:
            print(f"[{task["id"]}] ({task["status"]}) - {task["description"]}")
def main():
    parser = argparse.ArgumentParser(description="🧰 Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("description", type=str, help="Description of the task")

    # Update
    parser_update = subparsers.add_parser("update", help="Update an existing task")
    parser_update.add_argument("id", type=int, help="Task ID to update")
    parser_update.add_argument("--title", type=str, help="New description")
    parser_update.add_argument("--status", type=str, choices=["todo", "in-progress", "done"], help="New status")

    # Delete
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("id", type=int, help="Task ID to delete")

    # List
    parser_list = subparsers.add_parser("list", help="List all tasks")

    # Done Tasks
    parse_done = subparsers.add_parser("done", help="List all done tasks")

    # Done Tasks
    parse_progress = subparsers.add_parser("in-progress", help="List all in-progress tasks")

    # Done Tasks
    parse_todo = subparsers.add_parser("todo", help="List all todo tasks")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)
    elif args.command == "update":
        update_task(args.id, args.title, args.status)
    elif args.command == "delete":
        delete_task(args.id)
    elif args.command == "list":
        list_tasks()
    elif args.command == "done":
        tasks_status("done")
    elif args.command == "in-progress":
        tasks_status("in-progress")
    elif args.command == "todo":
        tasks_status("todo")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
