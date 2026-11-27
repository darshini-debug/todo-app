import functions
import FreeSimpleGUI as fs
import time

fs.theme("Black")
clock =fs.Text('',key='clock')
label=fs.Text("type in a to- do")
input_box=fs.InputText(tooltip="enter todo",key="todo")
add_buton =fs.Button("add")
list_box=fs.Listbox(values=functions.get_todo(),key='todos',
                      enable_events=True, size=[45, 10])
edit_button =fs.Button("edit")
complete_button=fs.Button("Complete")
exit_button =fs.Button("Exit")

window=fs.Window('My TO-DO  App',
                 layout=[[clock],
                          [label],
                          [input_box,add_buton],
                          [list_box, edit_button,complete_button],
                          [exit_button]],

                               font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

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
             try:
                    todo_to_edit = values['todos'][0]
                    new_todo = values['todo']
                    todos=functions.get_todo()
                    index= todos.index(todo_to_edit)
                    todos[index] = new_todo
                    functions.write_todo(todos)
                    window['todos'].update(values=todos)
             except IndexError:
                 fs.popup("please select the item" ,font=("Helvetica", 20))
        case 'Complete':
                try:

                        todo_to_complete =values['todos'][0]
                        todos =functions.get_todo()
                        todos.remove(todo_to_complete)
                        functions.write_todo(todos)
                        window['todos'].update(values=todos)
                        window['todo'].update(value='')

                except IndexError:
                    fs.popup("please select the item" ,font=("Helvetica", 20))

        case 'Exit':
              break

        case 'todos':
            window['todo'].update(value=values['todos'][0])



        case fs.WIN_CLOSED:
            break






window.close()




