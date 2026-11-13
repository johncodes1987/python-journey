import json
import os

class Task:
    def __init__(self, title, done=False):
        self.title = title
        self.done = done
    
    def mark_done(self):
        self.done = True
    
    def __str__(self):
        status = "x" if self.done else " "
        return f"[{status}] {self.title}"

    def to_dict(self):
        return {
            "title": self.title,
            "done": self.done
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data.get("done", False))


class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_from_file()

    def add_task(self, title):
        if not title.strip():
            return False
        task = Task(title.strip())
        self.tasks.append(task)
        self.save_to_file()
        return True

    def complete_task(self, display_index):
        internal_index = display_index - 1
        if 0 <= internal_index < len(self.tasks):
            self.tasks[internal_index].mark_done()
            self.save_to_file()
            return True
        return False

    def delete_task(self, display_index):
        internal_index = display_index - 1
        if 0 <= internal_index < len(self.tasks):
            self.tasks.pop(internal_index)
            self.save_to_file()
            return True
        return False

    def get_tasks(self):
        return self.tasks

    def save_to_file(self):
        data = [task.to_dict() for task in self.tasks]
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_from_file(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    data = json.load(f)
                    self.tasks = [Task.from_dict(item) for item in data]
            except (json.JSONDecodeError, KeyError, TypeError):
                backup_name = f"{self.filename}.bak"
                print(f"\n[WARNING] '{self.filename}' is corrupted or has an invalid schema.")
                print(f"Backing up file to '{backup_name}' before resetting.")
                
                if os.path.exists(backup_name):
                    os.remove(backup_name)
                os.rename(self.filename, backup_name)
                
                self.tasks = []


def get_valid_task_index(manager, action_name):
    tasks = manager.get_tasks()
    if not tasks:
        print(f"\nNo tasks available to {action_name}.")
        return None

    print(f"\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

    user_input = input(f"Enter task number to {action_name}: ").strip()
    try:
        return int(user_input)
    except ValueError:
        print("Error: Please enter a valid integer.")
        return None


def main():
    manager = TaskManager("tasks.json")

    while True:
        print("\n=== Task Manager v2 (Polished) ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            tasks = manager.get_tasks()
            if not tasks:
                print("\nNo tasks found.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")

        elif choice == "2":
            title = input("Enter task title: ").strip()
            if manager.add_task(title):
                print("Task added successfully.")
            else:
                print("Error: Task title cannot be empty.")

        elif choice == "3":
            display_num = get_valid_task_index(manager, "complete")
            if display_num is not None:
                if manager.complete_task(display_num):
                    print(f"Task {display_num} marked as complete!")
                else:
                    print(f"Error: Task number {display_num} does not exist.")

        elif choice == "4":
            display_num = get_valid_task_index(manager, "delete")
            if display_num is not None:
                if manager.delete_task(display_num):
                    print(f"Task {display_num} deleted successfully!")
                else:
                    print(f"Error: Task number {display_num} does not exist.")

        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()