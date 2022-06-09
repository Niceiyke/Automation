import PySimpleGUI as sg

sg.theme('PythonPlus')
sg.set_options(font= 'Franklin 12',button_element_size=(6,3))
button_size=(5,3)

layout=[[sg.Text('Output', font='Franklin 30',expand_x=True, justification ='right',pad=(10,20))],
[sg.Button('Clear',key='-CLEAR-',expand_x=True),sg.Button('Enter',key='-Enter-',expand_x=True)],
[sg.Button('7',key='-7-',size=button_size),sg.Button('8',key='-8-',size=button_size),sg.Button('9',key='-9-',size=button_size),sg.Button('*',key='-*-',size=button_size)],
[sg.Button('4',key='-4-',size=button_size),sg.Button('5',key='-5-',size=button_size),sg.Button('6',key='-6-',size=button_size),sg.Button('/',key='-/-',size=button_size)],
[sg.Button('1',key='-1-',size=button_size),sg.Button('2',key='-2-',size=button_size),sg.Button('3',key='-3-',size=button_size),sg.Button('-',key='---',size=button_size)],
[sg.Button('0',key='-0-',expand_x=True),sg.Button('.',key='-.-',size=button_size),sg.Button('+',key='-+-',size=button_size)],

] 


window=sg.Window('Calculator',layout)

while True:
    event, values =window.read()
    if event== sg.WIN_CLOSED:
        break







window.close()