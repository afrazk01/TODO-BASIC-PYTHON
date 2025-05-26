import functions
while True:
    user_input = input("Enter a command (add, show, remove, edit, complete, quit): ").strip().lower()
    if user_input:

        if user_input.startswith("show"):
            try:
                todo_list = functions.read_file()
                if not todo_list:
                    print("No tasks found.")
            except FileNotFoundError:
                print("This is file not found. Please create a new file.")

        elif user_input.startswith("add"):
            item = user_input[4:].strip()
            if not item:
                print("Please provide a task to add.")
                continue
            try:
                functions.write_file(item)

            except FileNotFoundError:
                print("This is file not found. Please create a new file.")
                continue

        elif user_input.startswith("complete") or user_input.startswith("remove"):
            try:
                todo_list = functions.read_file()
                if not todo_list:
                    print("No tasks found.")
                    continue
            except FileNotFoundError:
                print("This is file not found. Please create a new file.")
                continue
            functions.remove_task(user_input, todo_list)

        elif user_input.startswith("edit"):
            todo_list = functions.readfile()
            if not todo_list:
                print("No tasks found.")
                continue
            task_no = int(input("Select the task number to edit: "))
            new_item = input("Enter the new task: ").strip()
            functions.edit_task(task_no, new_item, todo_list)

        elif user_input.startswith("quit"):
            print("Goodbye!")
            break

        else:
            print("Invalid command. Try again.")
