import functions
import FreeSimpleGUI as sg

label=sg.Text("type in a to- do")
input_box=sg.InputText(tooltip="enter todo")
add_buton =sg.Button("add")

window=sg.Window('My TO-DO  App',layout=[ [label],[input_box,add_buton]])
window.read()
window.close()