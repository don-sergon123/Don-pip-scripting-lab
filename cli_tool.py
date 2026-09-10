import argparse


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        self.tasks.append({"title": title, "completed": False})
        print(f"Task '{title}' added successfully.")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            print(f"Task #{index} marked as complete.")
        else:
            print(f"Error: Task index {index} out of range.")


def main():
    parser = argparse.ArgumentParser(description="CLI Task Manager")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add-task", help="Add a task")
    add_parser.add_argument("title", type=str, help="Title of task")

    complete_parser = subparsers.add_parser(
        "complete-task", help="Complete a task")
    complete_parser.add_argument("index", type=int, help="Index of task")

    args = parser.parse_args()
    manager = TaskManager()

    if args.command == "add-task":
        manager.add_task(args.title)
    elif args.command == "complete-task":
        manager.complete_task(args.index)


if __name__ == "__main__":
    main()
