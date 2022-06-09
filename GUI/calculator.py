import PySimpleGUI as sg

def create_window(theme):

    sg.theme(theme)
    sg.set_options(font= 'Franklin 12',button_element_size=(6,3))
    button_size=(5,3)
    window_size=(10,4)

    layout=[[sg.Text('',
    font='Franklin 30',
    expand_x=True, 
    justification ='right',
    pad=(10,20),
    right_click_menu =theme_menu, key='-TEXT-')],
    [sg.Button('Clear',expand_x=True),sg.Button('Enter',expand_x=True)],
    [sg.Button('7',size=button_size),sg.Button('8',size=button_size),sg.Button('9',size=button_size),sg.Button('*',size=button_size)],
    [sg.Button('4',size=button_size),sg.Button('5',size=button_size),sg.Button('6',size=button_size),sg.Button('/',size=button_size)],
    [sg.Button('1',size=button_size),sg.Button('2',size=button_size),sg.Button('3',size=button_size),sg.Button('-',size=button_size)],
    [sg.Button('0',expand_x=True),sg.Button('.',size=button_size),sg.Button('+',size=button_size)],

    ] 
    return sg.Window('Calculator',layout,window_size)
theme_menu= ['menu',['DarkGrey1','LightGrey2','Dark','random']]

window= create_window("DarkGrey1")

current_num =[]
current_operation=[]
new_result=[]
while True:
    event, values =window.read()
    if event== sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        window.close()
        window=create_window(event)


    if event in ['1','2','3','4','5','6','7','8','9','0','.']:
        current_num.append(event)
        num_string =''.join(current_num)
        window['-TEXT-'].update(num_string)
  

    if event in ['+','-','*','/']:
        if len(new_result)==0:
            current_operation.append(''.join(current_num))
            current_num=[]
            current_operation.append(event)
            window['-TEXT-'].update('')
            print(current_operation)
        else:
            new_result.append(''.join(event))
            print(new_result)

        

    if event =='Enter':
        if len(new_result)==0:
            current_operation.append(''.join(current_num))
            result=eval(''.join(current_operation))
            current_operation=[]
            current_num=[]
            new_result.append(str(result))
            window['-TEXT-'].update(result)
            print(new_result)
        else:

            new_result.append(''.join(current_num))
            result =eval(''.join(new_result))
            new_result=[]
            current_num=[]
            new_result.append(str(result))
            window['-TEXT-'].update(result)
          
                
            print(result)

    

    if event =='Clear':
        current_operation=[]
        current_num=[]
        new_result=[]
        window['-TEXT-'].update('')





window.close()