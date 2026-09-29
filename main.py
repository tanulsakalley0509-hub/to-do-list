tasks = []

def show_menu():
    print("\n-- TO DO LIST ---")
    print("1. add task")
    print("2. view task")
    print("3. mark task as done")
    print("4. delete task")
    print("5. exit")

def add_task():
    task = input("enter task: ")
    tasks.append({"task": task, "done": False})
    print(f"task '{task}' added!")

def view_task():
    if not tasks:
        print("no tasks yet")
        return
    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❌"
        print(f"{index}. {task['task']} [{status}]")

def mark_done():
    view_task()
    if not tasks:
        return
    try:
        index = int(input("enter task number to mark done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("marked as done!")
        else:
            print("invalid number!")
    except ValueError:
        print("please enter a valid number.")

def delete_task():
    view_task()
    if not tasks:
        return
    try:
        index = int(input("enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"deleted task: {removed['task']}")
        else:
            print("invalid number!")
    except ValueError:
        print("please enter a valid number")

while True:
    show_menu()
    choice = input("choose an option (1-5): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_task()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("goodbye!")
        break
    else:
        print("invalid choice. try again.")
