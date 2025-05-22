FILEPATH='files/todo.txt'


def read_file(file_path=FILEPATH):
    with open(file_path,'r') as file:
        todo_list=file.readlines()
    return todo_list 