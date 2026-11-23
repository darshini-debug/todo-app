import functions
import FreeSimpleGUI as fs

label=fs.Text("type in a to- do")
input_box=fs.InputText(tooltip="enter todo",key="todo")
add_buton =fs.Button("add")
list_box=fs.Listbox(values=functions.get_todo(),key='todos',
                      enable_events=True, size=[45, 10])
edit_button =fs.Button("edit")

window=fs.Window('My TO-DO  App',
                 layout=[ [label],[input_box,add_buton],[list_box, edit_button]],
                               font=('Helvetica', 20))
while True:
    event, values = window.read()

    print(1,event)
    print(2,values)
    print(3,values['todos'])
    match event:
        case 'add':
            todos = functions.get_todo()
            new_todo = values['todo'] +"\n"
            todos.append(new_todo)
            functions.write_todo(todos)
            window['todos'].update(values=todos)

        case 'edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos=functions.get_todo()
            index= todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todo(todos)
            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])



        case fs.WIN_CLOSED:
            break






window.close()




