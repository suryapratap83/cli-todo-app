import os

tasks = []


def load_task(tasks):
    if os.path.exists("tasks.txt"):

        with open("tasks.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split("|")
                tasks.append({"task": parts[0], "done": parts[1]})
 
        return tasks
    else:
        return []


def save_task(tasks):

    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task["task"] + "|" + str(task["done"]) + "\n")


tasks = load_task(tasks)

while True:
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark tasks done")
    print("4. Exit")

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
         for i, task in enumerate(tasks, 1):
            print(i, "|", task["task"], "|", "✅" if task["done"] == True else "❌")

        
         number=int(input("Enter task number: "))
         tasks[number - 1]["done"] = True
         save_task(tasks)
         print("Task change confirmed")
        
    elif choose == "4":
        print("Exiting!")
        exit()

    else:
        print("Invalid choice. Please enter 1-3.")