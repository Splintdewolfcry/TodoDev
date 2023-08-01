import PySimpleGUI as sg

label1 = sg.Text('Select File/Files to Compress')
input1 = sg.Input()
button1 = sg.FilesBrowse('Choose')

label2 = sg.Text('Select Destination Folder')
input2 = sg.Input()
button2 = sg.FolderBrowse('Choose')

compress_button = sg.Button('Compress')

window = sg.Window('File Compressor', 
                    layout = [[label1, input1, button1],
                             [label2, input2, button2],
                             [compress_button]])

window.read()
window.close()