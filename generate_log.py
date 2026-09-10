import argparse
from datetime import datetime
import requests

log_data = [
    "User logged in",
    "User updated profile",
    "Report exported"
]
filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

with open(filename, "w") as file:
    for entry in log_data:
        file.write(f"{entry}\n")

print(f"Log written to {filename}")


def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}


if __name__ == "__main__":
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        self.tasks.append({"title": title, "completed": False})
        print(f"Task '{title}' added successfully.")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            print(f"Task #{index + 1} marked as complete.")
        else:
            print(f"Error: Task index {index + 1} not found.")


def main():
    parser = argparse.ArgumentParser(description="CLI Task Manager")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add-task", help="Add a new task")
    add_parser.add_argument("title", type=str, help="Title of the task")

    complete_parser = subparsers.add_parser(
        "complete-task", help="Mark a task as complete")
    complete_parser.add_argument(
        "index", type=int, help="Task index to complete")

    args = parser.parse_args()
    manager = TaskManager()

    if args.command == "add-task":
        manager.add_task(args.title)
    elif args.command == "complete-task":
        manager.complete_task(args.index - 1)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
