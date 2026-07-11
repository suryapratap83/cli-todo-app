import os

# ── Storage ──────────────────────────────────────────────────────────────────

tasks = []

def load_task(tasks):
    """Read tasks from tasks.txt and load them into memory on startup."""
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                # Each line is stored as: task_name|done_status
                parts = line.strip().split("|")
                tasks.append({"task": parts[0], "done": parts[1]})
        return tasks
    else:
        # No file yet — start with empty list
        return []


def save_task(tasks):
    """Write all tasks to tasks.txt to persist between sessions."""
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task["task"] + "|" + str(task["done"]) + "\n")


# ── Startup ───────────────────────────────────────────────────────────────────

# Load any previously saved tasks before showing the menu
tasks = load_task(tasks)


# ── Main Loop ─────────────────────────────────────────────────────────────────

while True:
    # Display menu options
    print("\n─────────────────────────")
    print("     CLI To-Do App")
    print("─────────────────────────")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task done")
    print("4. Delete task")
    print("5. Search task")
    print("6. Exit")
    print("─────────────────────────")

    choose = input("Choose: ")

    # ── Option 1: Add Task ────────────────────────────────────────────────────
    if choose == "1":
        while True:
            task = input("Enter task: ")

            # Don't allow blank tasks
            if task.strip() == "":
                print("Task cannot be empty!")
                continue

            # Add task as not done by default
            tasks.append({"task": task, "done": False})
            save_task(tasks)
            print("✅ Task added!")

            add_another = input("Add another? (y/n): ")

            if add_another.lower() == "n":
                break
            elif add_another.lower() == "y":
                continue
            else:
                print("Please enter y or n.")
                add_another = input("Add another? (y/n): ")

    # ── Option 2: View Tasks ──────────────────────────────────────────────────
    elif choose == "2":
        if len(tasks) == 0:
            print("No tasks yet — add one!")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, 1):
                status = "✅" if task["done"] == True else "❌"
                print(f"  {i} | {task['task']} | {status}")

    # ── Option 3: Mark Task Done ──────────────────────────────────────────────
    elif choose == "3":
        # Show all tasks first so user knows which number to pick
        for i, task in enumerate(tasks, 1):
            status = "✅" if task["done"] == True else "❌"
            print(f"  {i} | {task['task']} | {status}")

        while True:
            try:
                number = int(input("Task number to mark done: "))
            except ValueError:
                print("Please enter a valid number!")
                continue

            # Check if number is within valid range
            if number < 1 or number > len(tasks):
                print("Invalid task number!")
                continue

            tasks[number - 1]["done"] = True
            save_task(tasks)
            print("✅ Task marked as done!")
            break

    # ── Option 4: Delete Task ─────────────────────────────────────────────────
    elif choose == "4":
        # Show all tasks first so user knows which number to pick
        for i, task in enumerate(tasks, 1):
            status = "✅" if task["done"] == True else "❌"
            print(f"  {i} | {task['task']} | {status}")

        while True:
            try:
                number1 = int(input("Task number to delete: "))
            except ValueError:
                print("Please enter a valid number!")
                continue

            # Check if number is within valid range
            if number1 < 1 or number1 > len(tasks):
                print("Invalid task number!")
                continue

            # Remove task from list and update file
            tasks.pop(number1 - 1)
            save_task(tasks)
            print("🗑️  Task deleted!")
            break

    # ── Option 5: Search Task ─────────────────────────────────────────────────
    elif choose == "5":
        try:
            choose_task = int(input("Enter task number to search: "))
            if 1 <= choose_task <= len(tasks):
                task = tasks[choose_task - 1]
                status = "✅" if task["done"] else "❌"
                print(f"  {choose_task} | {task['task']} | {status}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number!")

    # ── Option 6: Exit ────────────────────────────────────────────────────────
    elif choose == "6":
        print("Goodbye! 👋")
        exit()

    else:
        print("Invalid choice. Please enter 1-6.")







