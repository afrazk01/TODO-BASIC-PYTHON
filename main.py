from functions import read_file
while True:
    user_input = input("Enter a command (add, show, remove, edit, complete, quit): ").strip().lower()
    if user_input:

        if user_input.startswith("show"):
            try:
                todo_list = read_file()
                if not todo_list:
                    print("No tasks found.")
                else:
                    for index, item in enumerate(todo_list):
                        print(f"{index+1}: {item.strip()}")
            except FileNotFoundError:
                print("This is file not found. Please create a new file.")

        if user_input.startswith("add"):
            item = input("Enter the task to add: ").strip()
            with open("files/todo.txt", "a") as file:
                file.write(item + "\n")
            print(f"Added '{item}' to the list.")

        if user_input.startswith("complete") or user_input.startswith("remove"):
            try:
                todo_list = read_file()
                if not todo_list:
                    print("No tasks found.")
                    continue
                if todo_list:
                    for index, item in enumerate(todo_list):
                        print(f"{index+1}: {item.strip()}")
            except FileNotFoundError:
                print("This is file not found. Please create a new file.")
                continue
            task_no = int(input("Select the task number to remove: "))
            todo_list.pop(task_no - 1)
            with open("files/todo.txt", "w") as file:
                file.writelines(todo_list)
            print("Task removed.")

        if user_input.startswith("edit"):
            with open("files/todo.txt", "r") as file:
                todo_list = file.readlines()
            for index, item in enumerate(todo_list):
                print(f"{index+1}: {item.strip()}")
            task_no = int(input("Select the task number to edit: "))
            new_item = input("Enter the new task: ").strip()
            todo_list[task_no - 1] = new_item + "\n"
            with open("files/todo.txt", "w") as file:
                file.writelines(todo_list)
            print("Task updated.")

        if user_input.startswith("quit"):
            print("Goodbye!")
            break

        else:
            print("Invalid command. Try again.")
