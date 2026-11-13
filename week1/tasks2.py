def show_tasks(tasks):
    print("\nYour Task List:")
    for index, task in enumerate(tasks, start=1):
        status = "x" if task["done"] else " "
        print(f"{index}. [{status}] {task['title']}")

tasks = []

while True:
    task_input = input("Add a task (or type 'quit'): ").strip()
    
    if task_input.lower() == "quit":
        break
    
    if task_input == "":
        continue
    
    tasks.append({"title": task_input, "done": False})
    

show_tasks(tasks)