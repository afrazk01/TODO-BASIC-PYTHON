while True:
    user_input = input("Enter a command (add, show, remove, edit, complete, quit): ").strip().lower()

    match user_input:

        case "show":
            with open("files/todo.txt", "r") as file:
                todo_list = file.readlines()
                print("This is how readlines looks like:", todo_list)
                for index, item in enumerate(todo_list):
                    print(f"{index+1}: {item.strip()}")

        case "add":
            item = input("Enter the task to add: ").strip()
            with open("files/todo.txt", "a") as file:
                file.write(item + "\n")
            print(f"Added '{item}' to the list.")

        case "remove" | "complete":
            with open("files/todo.txt", "r") as file:
                todo_list = file.readlines()
            for index, item in enumerate(todo_list):
                print(f"{index+1}: {item.strip()}")
            task_no = int(input("Select the task number to remove: "))
            todo_list.pop(task_no - 1)
            with open("files/todo.txt", "w") as file:
                file.writelines(todo_list)
            print("Task removed.")

        case "edit":
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

        case "quit":
            print("Goodbye!")
            break

        case _:
            print("Invalid command. Try again.")
