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
        """Converts the task instance into a dictionary for JSON storage."""
        return {
            "title": self.title,
            "done": self.done
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a new Task instance from a dictionary loaded from JSON."""
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
        """
        Takes a 1-based user index, converts it to 0-based internal index,
        completes the task, and returns True on success or False on failure.
        """
        internal_index = display_index - 1
        if 0 <= internal_index < len(self.tasks):
            self.tasks[internal_index].mark_done()
            self.save_to_file()
            return True
        return False

    def get_tasks(self):
        """Returns the task list so the UI layer can handle display (Separation of Concerns)."""
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
            except json.JSONDecodeError:
                # Point 3: Prevent data loss by warning, backing up, and starting fresh
                backup_name = f"{self.filename}.bak"
                print(f"\n[WARNING] '{self.filename}' contains corrupted JSON data.")
                print(f"Backing up corrupted file to '{backup_name}' before resetting.")
                
                if os.path.exists(backup_name):
                    os.remove(backup_name)
                os.rename(self.filename, backup_name)
                
                self.tasks = []


def main():
    manager = TaskManager()

    while True:
        print("\n=== Task Manager ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            tasks = manager.get_tasks()
            if not tasks:
                print("\nNo tasks found.")
            else:
                print("\nYour Tasks:")
                # Point 4: 1-based display counting for humans using enumerate(..., 1)
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")

        elif choice == "2":
            title = input("Enter task title: ").strip()
            if manager.add_task(title):
                print("Task added successfully.")
            else:
                print("Error: Task title cannot be empty.")

        elif choice == "3":
            tasks = manager.get_tasks()
            if not tasks:
                print("\nNo tasks available to complete.")
                continue

            try:
                display_num = int(input("Enter task number to complete: "))
                # Point 2: Check boolean return value to handle success/failure messages in the menu
                if manager.complete_task(display_num):
                    print(f"Task {display_num} marked as complete!")
                else:
                    print(f"Error: Task number {display_num} does not exist.")
            except ValueError:
                print("Error: Please enter a valid integer.")

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()