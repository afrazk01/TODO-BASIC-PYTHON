todo_list = []

while True:
    user_input = input("Enter a command (add, remove, show, quit): ").strip().lower()
    match user_input:
        case "show":
            for item in todo_list:
                print(item)
        case "add":
            item = input("Enter the item to add: ").strip()
            todo_list.append(item)
            print(f"Added '{item}' to the list.")
        case "remove":
            print("These are the Item available to remove:")
            for item in todo_list:
                print(item)
            item = input("Enter the item to remove: ").strip()
            if item in todo_list:
                todo_list.remove(item)
                print(f"Removed '{item}' from the list.")
            else:
                print(f"'{item}' not found in the list.")
        case "quit":
            break