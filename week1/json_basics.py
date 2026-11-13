import json

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=2)

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

if __name__ == "__main__":
    sample_tasks = [
        {"title": "Learn JSON file handling", "done": True},
        {"title": "Build persistent task manager", "done": False}
    ]
    
    save_tasks(sample_tasks)
    print("Tasks saved successfully.")
    
    loaded = load_tasks()
    print("Loaded tasks from file:", loaded)