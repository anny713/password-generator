import random
import string
import PySimpleGUI as sg

upper = random.sample(string.ascii_uppercase,2)
lower = random.sample(string.ascii_lowercase,2)
digits = random.sample(string.digits,2)
symbols = random.sample(string.punctuation,2)

total = upper+lower+digits+symbols
total = random.sample(total, len(total))
total = ''.join(total)
print(total) 


layout = [
  
[sg.Text('Uppercase:'), sg.Input()],
[sg.Text('Lowercase:'), sg.Input()],
[sg.Text('Digits:'), sg.Input()],
[sg.Text('Symbols:'), sg.Input()],
[sg.Button('Ok'), sg.Button('Cancel')],
[sg.Text('Password'),sg.Multiline]
]

window = sg.Window('Password Generator', layout)

window.read()

window.close()
