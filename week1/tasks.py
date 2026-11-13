tasks = []

while True:
    task = input("Add a task (or type 'quit'): ")
    if task.lower() == "quit":
        break
    tasks.append(task)

print("\nYour Task List:")
for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")