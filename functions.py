FILEPATH='files/todo.txt'


def read_file(file_path=FILEPATH):
    with open(file_path,'r') as file:
        todo_list=file.readlines()
    if todo_list:
        for index, item in enumerate(todo_list):
            print(f"{index+1}: {item.strip()}")
    return todo_list 

def write_file(item, file_path=FILEPATH):
    with open(file_path,'a') as file:
        file.write(item + '\n')
    print(f"Added task: {item}")

def remove_task(userinput, todo_list, file_path=FILEPATH):
    try:
        task_no = int(userinput[7:].strip())
    except ValueError:
        print("Please provide a valid task number.")
        return
    if task_no < 1 or task_no > len(todo_list):
        print("Invalid task number.")
        return
    print(f"Removing task: {todo_list[task_no - 1].strip()}")
    todo_list.pop(task_no - 1)
    with open(file_path, "w") as file:
        file.writelines(todo_list)
    print("Task removed.")

def edit_task(task_no, new_item, todo_list, file_path=FILEPATH):
    todo_list[task_no - 1] = new_item + "\n"
    with open(file_path, "w") as file:
        file.writelines(todo_list)
    print("Task updated.")

if __name__ == "__main__":
    # Example usage
    todo_list = read_file()
    if not todo_list:
        print("No tasks found.")
    else:
        print("Tasks loaded successfully.")
        # Add more functionality as needed