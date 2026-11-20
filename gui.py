import functions
import FreeSimpleGUI as fs

label=fs.Text("type in a to- do")
input_box=fs.InputText(tooltip="enter todo",key="todo")
add_buton =fs.Button("add")

window=fs.Window('My TO-DO  App',
                 layout=[ [label],[input_box,add_buton]],
                               font=('Helvetica', 20))
while True:
    event, values = window.read()

    print(event)
    print(values)

    match event:
        case 'add':
            todos = functions.get_todo()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todo(todos)

        case fs.WIN_CLOSED:
            break






window.close()




