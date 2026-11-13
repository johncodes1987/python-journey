import json

# Unsafe load function without try/except
def load_tasks_unsafe():
    with open("tasks.json", "r") as f:
        return json.load(f)

load_tasks_unsafe()