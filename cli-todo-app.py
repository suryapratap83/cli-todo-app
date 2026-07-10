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
    print("1.Add task")
    print("2.View task")
    print("3.Mark task done")
    print("4.Delete task")
    print("5.Search task")
    print("6.Exit")

    choose = input("Choose: ") 

    if choose == "1":
        while True:
            task = input("Enter task: ")
            if task.strip() == "":
             print("Task cannot be empty!")
             continue
            tasks.append({"task": task, "done": False})
            save_task(tasks)
            print("Task added")

            add_another = input("Add another (y/n): ")

            if add_another.lower() == "n":
                break
            elif add_another.lower() == "y":
                continue
            else:
                print("Please enter y/n")
                add_another = input("Add another (y/n): ")

    elif choose == "2":
        if len(tasks) == 0:
            print("No tasks yet!")
        else:
            for i, task in enumerate(tasks, 1):
                print(i, "|", task["task"], "|", "✅" if task["done"] == True else "❌")

    elif choose == "3":
        for i, task in enumerate(tasks, 1):
            print(i, "|", task["task"], "|", "✅" if task["done"] == True else "❌")

        while True:
            try:
                number = int(input("Task to change: "))
            except ValueError:
                print("Please enter a valid number!")
                continue

            if number < 1 or number > len(tasks):
                print("Invalid task number!")
                continue

            tasks[number - 1]["done"] = True
            save_task(tasks)
            print("Task change confirmed")
            break

    elif choose == "4":
        
        for i, task in enumerate(tasks, 1):
            print(i, "|", task["task"], "|", "✅" if task["done"] == True else "❌")

        while True:
            try:
                number1 = int(input("Task to delete: "))
            except ValueError:
                print("Please enter a valid number!")
                continue

            if number1 < 1 or number1 > len(tasks):
                print("Invalid task number!")
                continue

            
            tasks.pop(number1 - 1)
            save_task(tasks)
            print("Task was deleted")
            break
    elif choose == "5":
         choose_task = int(input("Choose_task: "))
         if 1 <= choose_task <= len(tasks):
             task = tasks[choose_task - 1]
             print(choose_task, "|", task["task"], "|", "✅" if task["done"] else "❌")
         else:
              print("Invalid task number.")
                

    elif choose == "6":
        print("Exiting")
        exit()

    else:
        print("Invalid choice. Please enter 1-5.")







