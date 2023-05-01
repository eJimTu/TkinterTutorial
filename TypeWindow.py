import tkinter as tk
from tkinter import ttk

def buttonFunc():
    entry_text = entry.get()
    label['text'] = entry_text
    entry['state'] = 'disabled'

def buttonFunc2():
    label['text'] = 'some Text'
    entry['state'] = 'enabled'


window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x600')

#ttk widgets
label = ttk.Label(master = window, text='Some text', font='Calibri 24 bold')
label.pack()

#create widgets
text = tk.Text(master = window)
text.pack()

#ttk entry
entry = ttk.Entry(master = window)
entry.pack()

#exercise Label
Label_ex = ttk.Label(master = window, text='my Label')
Label_ex.pack()

#ttk button
button = ttk.Button(master=window, text='Button', command = buttonFunc)
button.pack()

#exercise button

button_ex = ttk.Button(master = window, text = 'Say Hello', command = buttonFunc2)
button_ex.pack()

#run
window.mainloop()