import tkinter as tk
from tkinter import ttk

#setup 
window = tk.Tk()
window.title('Buttons')
window.geometry('600x400')

#button
def ButtonFunc():
    print('A basic button')
    print(RadioVar1.get())


buttonString = tk.StringVar(value = 'A button with StringVar')
button = ttk.Button(master = window, text = 'A simple button', command = ButtonFunc, textvariable= buttonString)
button.pack()

#checkbutton

checkVar = tk.IntVar()
check1= ttk.Checkbutton(master = window,
                        text='Checkkbox1', 
                        command = lambda: print(checkVar.get()),
                        variable=checkVar,
                        onvalue = 10,
                        offvalue = 5   )

check2 = ttk.Checkbutton(window, 
                         text='Checkbutton2',
                         command=lambda: print('test'))
check1.pack()
check2.pack()

#radiobutton
RadioVar1 = tk.StringVar()
radio1 = ttk.Radiobutton(window, 
                         text='Radiobutton 1', 
                         value = 'radio1', 
                         command = lambda: print(RadioVar1.get()))
radio2 = ttk.Radiobutton(window, text='Radiobutton 2', value = 2, variable = RadioVar1)

radio1.pack()
radio2.pack()

#exercise
def CheckFunc():
    print(ExCheckVar.get())
    ExCheckVar.set(False)




ExCheckVar = tk.BooleanVar(value = False)
ExRadioVar = tk.StringVar()

ExRadio1 = ttk.Radiobutton(window,
                        text = 'Radiobutton A', 
                        value = 'A', 
                        command = CheckFunc, 
                        variable=ExRadioVar)

ExRadio2 = ttk.Radiobutton(window, 
                           text='Radiobutton B', 
                           value = 'B', 
                           command = CheckFunc, 
                           variable=ExRadioVar)

ExCheck = ttk.Checkbutton(window, 
                          text = 'Checkbutton Exercise', 
                          command = lambda: print(ExRadioVar.get()), 
                          variable=ExCheckVar)

ExRadio1.pack()
ExRadio2.pack()
ExCheck.pack()



#run
window.mainloop()
