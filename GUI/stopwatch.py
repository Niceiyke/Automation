import PySimpleGUI as sg

sg.theme('dark')
layout=[

[sg.VPush()],
[sg.Text('time',key='-TEXT-'),
],
[sg.Button('Start'),sg.Button('Lap')],
[sg.VPush()]

] 


window=sg.Window('Stopwatch',
layout,
size=(300,300),
no_titlebar=True,element_justification='center')

while True:
    event, values =window.read()
    if event in (sg.WIN_CLOSED,'Start'):
        break
  

window.close()