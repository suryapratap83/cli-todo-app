tasks = []

while True:
    print("1. Add task")
    print("2. View tasks")
    print("3. Exit")

    choose = input("Choose: ")

    if choose == "1":
        task = input("Enter task: ")
        tasks.append({"task": task, "done": False})
        print("Task added!")

    elif choose == "2":
        if len(tasks) == 0:
            print("No tasks yet!")
        else:
            for i, task in enumerate(tasks, 1):
                print(i, "|", task["task"], "|", "✅" if task["done"] else "❌")

    elif choose == "3":
        print("Exiting!")
        exit()

    else:
        print("Invalid choice. Please enter 1-3.")