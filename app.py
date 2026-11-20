from functions import get_todo ,write_todo
import time

now=time.strftime("%Y-%b-%d %H:%M:%Ss")

print("IT IS :" ,now)


while True:
    user_action=input("enter add or show or edit or complete or  exit: ")
    user_action=user_action.strip()   #to remove th space from the user input line "add " like "add"


    if user_action.startswith('add'):
        todo=user_action[4:]

        todos = get_todo()                                                   #file=open('todo.txt','r')
                                                            #todos = file.readlines()
                                                           #file.close()
        todos.append(todo+"\n")
        print(todos)
         #file=open('todo.txt','w')
        write_todo(todos)
                                                      #file.writelines(todos)
                                                       #file.close()
    elif user_action.startswith('show'):
        todos=get_todo()
        #new_todo=[]
        #for item in todos:
         #   new_item=item.strip("\n")
          #  new_todo.append(new_item)
        #instead

        #new_todos=[item.strip("\n") for item in todos]
        #instead
        for index,i in enumerate(todos):  #get the index along with the list
            i=i.strip("\n")   # we can add this strip here
            print(f"{index+1}-{i}")
    elif user_action.startswith('edit'):
        try:
            number=int(user_action[5:])
            number=number-1
            todos=get_todo("todo.txt")
            print(todos)
            new_todo=input("enter the new todo: ")
            todos[number]=new_todo+'\n'
            write_todo( todos)

            print(todos)
        except ValueError:
            print("please enter a valid input")
        continue
    elif  user_action.startswith('complete'):
       try:
            number=int(user_action[9:])

            todos=get_todo()

            index = number - 1
            todo_to_remove=todos[index].strip('\n')
            todos.pop(index)

            write_todo(todos)

            message=f"number is removed from the list is : {todo_to_remove}"
            print(message)
       except IndexError:
           print("please enter a valid index")
           continue

    elif  user_action.startswith('exit'):
        break

    elif  user_action.startswith('_'):
        print("please enter a valid input")

    else:
        print("please enter a valid input")
print("byee")