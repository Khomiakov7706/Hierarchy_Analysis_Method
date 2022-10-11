import PySimpleGUI as sg
import hierarchy_analysis

layout = [
    [sg.Text('criteria number\t'), sg.InputText(),
     sg.Checkbox('input criteria names')
     ],
    [sg.Text('alternatives number\t'), sg.InputText(),
     sg.Checkbox('input alternatives names')
     ],
    #[sg.Output(size=(88, 20))],
    [sg.Submit(), sg.Cancel()]
]
window = sg.Window('File Compare', layout)
"""event, values = window.read()
if event in ('Submit'):
    print(event, values) #debug
elif event in ('Exit', 'Cancel'):
    window.close()
#sg.popup_ok('popup_ok')
"""