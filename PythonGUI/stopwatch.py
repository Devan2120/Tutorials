import PySimpleGUI as sg
from time import time

def create_window():

    sg.theme('black')
    layout = [[sg.Push(), sg.Image('./extras/cross.png', pad = 0, enable_events = True, key = '-CLOSE-')],
            [sg.VPush()],
            [sg.Text('0.0', font = 'Young 30', key = '-TIME-')],
            [sg.Button('Start', button_color = ('#FFFFFF','#FF0000'), border_width = 0, key = '-START-'),sg.Button('Lap', button_color = ('#FFFFFF','#FF0000'), border_width = 0, key = '-LAP-', visible = False)],
            [sg.Column([[]], key = '-LAPS-')],
            [sg.VPush()],]
    
    return  sg.Window("Stopwatch", layout, size = (300,300), no_titlebar = True,
                element_justification = 'center')

window = create_window()

start_time = 0
active = False
lap_no = 0

while True:
    event, values = window.read(timeout = 10)
    if event in (sg.WIN_CLOSED, '-CLOSE-'):
        break

    if event == '-START-':
        if active:
            active = False
            window['-START-'].update('Reset')
            window['-LAP-'].update(visible = False)
        else:
            if start_time > 0:
                window.close()
                window = create_window()
                start_time = 0
                lap_no = 1
            else:
                start_time = time()
                active = True
                window['-START-'].update('STOP')
                window['-LAP-'].update(visible = True)

    if active:
        elapsed_time = round(time() - start_time, 1)
        window['-TIME-'].update(elapsed_time)

    if event == '-LAP-':
        window.extend_layout(window['-LAPS-'], [[sg.Text(lap_no),sg.VSeparator(), sg.Text(elapsed_time)]])
        lap_no += 1

window.close() 