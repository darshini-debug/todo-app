import functions
import FreeSimpleGUI as fs

label=fs.Text("type in a to- do")
input_box=fs.InputText(tooltip="enter todo")
add_buton =fs.Button("add")

window=fs.Window('My TO-DO  App',layout=[ [label],[input_box,add_buton]])
window.read()
window.close()


