import PySimpleGUI as sg

layout=[[sg.Input(key = '-INPUT-'), 
         sg.Spin(['km-mile','kg-pound','sec-min'], key = '-UNITS-'),
         sg.Button('Convert', key = '-CONVERT-')
         ],
        [sg.Text('Output', key = '-OUTPUT-')]]

window = sg.Window("Converter",layout)

while True:
    event, values = window.read()
    if event ==sg.WIN_CLOSED:
        break

    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            match values['-UNITS-']:
                case 'km-mile':
                    output= round(float(input_value) * 0.6214,3)
                    output_string = f'{input_value} km are {output} miles.'
            
                case 'kg-pound':
                    output= round(float(input_value) * 2.20462,3)
                    output_string = f'{input_value} kg are {output} pound.'
                
                case 'sec-min':
                    output= round(float(input_value) / 60,3)
                    output_string = f'{input_value} sec are {output} minute.'

            window['-OUTPUT-'].update(output_string)

        else:
            window['-OUTPUT-'].update('Please enter a Number')
window.close()