FILEPATH="todo.txt"

def get_todo(filepath=FILEPATH):          # rather than repitating the code we can have custom function
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todo(todo_local, filepath=FILEPATH):
    with open(filepath,'w') as file:
        file.writelines(todo_local)

if __name__=="__main__":
    print(get_todo())