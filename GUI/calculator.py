import PySimpleGUI as sg

def create_window(theme):

    sg.theme(theme)
    sg.set_options(font= 'Franklin 12',button_element_size=(6,3))
    button_size=(5,3)

    layout=[[sg.Text('Output',
    font='Franklin 30',
    expand_x=True, 
    justification ='right',
    pad=(10,20),
    right_click_menu =theme_menu )],
    [sg.Button('Clear',expand_x=True),sg.Button('Enter',expand_x=True)],
    [sg.Button('7',size=button_size),sg.Button('8',size=button_size),sg.Button('9',size=button_size),sg.Button('*',size=button_size)],
    [sg.Button('4',size=button_size),sg.Button('5',size=button_size),sg.Button('6',size=button_size),sg.Button('/',size=button_size)],
    [sg.Button('1',size=button_size),sg.Button('2',size=button_size),sg.Button('3',size=button_size),sg.Button('-',size=button_size)],
    [sg.Button('0',expand_x=True),sg.Button('.',size=button_size),sg.Button('+',size=button_size)],

    ] 
    return sg.Window('Calculator',layout)
theme_menu= ['menu',['DarkGrey1','LightGrey2','Dark','random']]

window= create_window("DarkGrey1")

while True:
    event, values =window.read()
    if event== sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        window.close()
        window=create_window(event)


    if event in ['1','2','3','4','5','6','7','8','9','0','.']:
        print(event)

    if event in ['+','-','*','/']:
        print(event)

    if event =='Clear':
        print(event)

    if event =='Enter':
        print(event)




window.close()