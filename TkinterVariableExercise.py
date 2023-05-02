import tkinter as tk
from tkinter import ttk

def ButtonFunc():
    print(StringVar.get())
#window
window = tk.Tk()
window.title('Tkinter Variables')

#Tkinter Variable
StringVar = tk.StringVar()

#Exercise Tkinter Variable
ExStringVar = tk.StringVar(value = 'test')


#Widgets
Label =ttk.Label(master = window , text= 'Exercise Label', textvariable=StringVar) #using the stringvar updates all widgets using this variable
Entry = ttk.Entry(master = window, textvariable=StringVar)#variable is changed by typing in the entry field
Button = ttk.Button( master = window, text = 'Button', command = ButtonFunc)

#exercise widgets

ExEntry1 = ttk.Entry(master = window, textvariable=ExStringVar)
ExEntry2 = ttk.Entry(master =window, textvariable=ExStringVar)
ExLabel = ttk.Label(master = window, text = 'test', textvariable= ExStringVar)

Label.pack()
Entry.pack()
Button.pack()

ExEntry1.pack()
ExEntry2.pack()
ExLabel.pack()
#run
window.mainloop()