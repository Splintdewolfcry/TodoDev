from functions import get_todos, write_todos
import PySimpleGUI as sg


label = sg.Text("Enter your todo")
input_box = sg.InputText(tooltip='Enter To-do', key='todo')
add_button = sg.Button('Add')

window = sg.Window("My Todo App",
                layout=[[label, input_box, add_button]],
                font = ('Times New Roman', 12))

while True:
    event, values = window.read()

    match event:
        case 'Add':
            todos = get_todos('todos.txt')

            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            write_todos(todos)
        case sg.WIN_CLOSED:
            break



print(window.read())
window.close()