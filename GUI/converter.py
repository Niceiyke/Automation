import PySimpleGUI as sg

layout=[
[
sg.Input(key='-INPUT-'),
sg.Spin(['KG-Pound','Sec-Min','Km-Mile'],key='-UNITS-'),
sg.Button('Convert',key='-CONVERT-')
],
[sg.Text('Result',key='-OUTPUT-')]
] 


window=sg.Window('Converter',layout)

while True:
    event, values =window.read()
    if event== sg.WIN_CLOSED:
        break
    if event=='-CONVERT-':
        input_value =values['-INPUT-']
        if input_value.isnumeric():
            if values['-UNITS-']=='KG-Pound':
                output=round(float(input_value) *2.20462,2)
                output_string = f'{input_value} KG are {output} Pound'
            
            elif values['-UNITS-']=='Km-Mile':
                output=round(float(input_value) *0.6214,2)
                output_string = f'{input_value} KM are {output} Mile'

            elif values['-UNITS-']=='Sec-Min':
                output=round(float(input_value) /60,2)
                output_string = f'{input_value} Sec are {output} Min'

        else: 
            window['-OUTPUT-'].update('Please Enter a number')

window.close()