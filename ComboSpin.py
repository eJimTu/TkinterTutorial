import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('500x400')
window.title('Combo and Spin')

# Combobox
items = ('Ice Cream', 'Pizza', 'Broccoli')
foodString = tk.StringVar(value = items[0])
combo = ttk.Combobox(window, textvariable=foodString)
combo['values'] = items
combo.pack()

combo.bind('<<ComboboxSelected>>', lambda event: comboLabel.configure(text=f'Selected value: {foodString.get()}'))
comboLabel = ttk.Label(window, text = 'a label')
comboLabel.pack()

#Spinbox
spinInt = tk.IntVar(value=12)
spin = ttk.Spinbox(window, 
                   from_ = 3, 
                   to = 20, increment=2,
                   command= lambda: print(spinInt.get()), 
                   textvariable=spinInt)
spin.bind('<<Increment>>', lambda event : print('up'))
spin.bind('<<Decrement>>', lambda event: print('down'))
#spin['value']
spin.pack()

#exercise
ExSpinString = tk.StringVar(value = 'A')
ExSpin = ttk.Spinbox(window, textvariable= ExSpinString)
ExSpin['value'] = ('A','B','C','D','E')

ExSpin.bind('<<Decrement>>', lambda event: print(ExSpinString.get()))
ExSpin.pack()
window.mainloop()