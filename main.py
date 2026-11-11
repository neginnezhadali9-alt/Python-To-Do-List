# To-D0 List

tasks = []

while True:

    print("\n===== MY TO-DO LIST =====")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Complte tasks")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Goodby!")
        break

    elif choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("Your to-do list is empty!")
        else:
            for number, task in enumerate(tasks, start = 1):
                print(f"{number}. {task}")

    elif choice == "3":
            try :
                 task_number = int(input("Enter task number:"))
                 if task_number >= 1 and task_number <= len(tasks):
                      index = task_number - 1
                      tasks[index] = "[Done]" + tasks[index]
                      print("Task completed successfully")
                 else :
                     print("Invalid task number")
            except ValueError:
                print("Please enter a valid numbers")

    elif choice == "4":
        try:
            task_number = int(input("Enter task number: "))
            if task_number >= 1 and task_number <= len(tasks):
                index = task_number - 1
                tasks.pop(index)
                print("Task deleted successfully!")
            else:
                print("Invalid task number")

        except ValueError:
            print("Please enter a valid number!")
