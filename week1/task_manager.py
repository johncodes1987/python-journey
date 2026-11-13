# task_manager.py
import json

FILENAME = "tasks.json"

def load_tasks():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=2)

def show_tasks(tasks):
    if not tasks:
        print("\nYour task list is currently empty!")
        return
    print("\n--- Your Task List ---")
    for index, task in enumerate(tasks, start=1):
        status = "x" if task["done"] else " "
        print(f"{index}. [{status}] {task['title']}")
    print("-" * 22)

def main():
    tasks = load_tasks()
    
    while True:
        print("\nTask Manager Menu:")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Mark task done")
        print("4. Quit")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            show_tasks(tasks)
            
        elif choice == "2":
            title = input("Enter the task description: ").strip()
            if not title:
                print("Task description cannot be empty.")
                continue
            tasks.append({"title": title, "done": False})
            save_tasks(tasks)
            print(f"Added: '{title}'")
            
        elif choice == "3":
            if not tasks:
                print("No tasks available to mark as done.")
                continue
            show_tasks(tasks)
            try:
                num = int(input("Enter the task number to mark done: "))
                if 1 <= num <= len(tasks):
                    tasks[num - 1]["done"] = True
                    save_tasks(tasks)
                    print(f"Task {num} marked as done!")
                else:
                    print(f"Invalid task number. Please enter a number between 1 and {len(tasks)}.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()