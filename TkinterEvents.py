import tkinter as tk
from tkinter import ttk

def getPos(event):
    print(f'x: {event.x} y: {event.y}')


#init
window = tk.Tk()
window.title('Event Binding')
window.geometry('800x600')

#widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text= 'A button')
button.pack()

#events
#button.bind('<Alt-KeyPress-a>', lambda event: print(event)) #triggered wenn Alt + a is pressed
window.bind('<Motion>', getPos)

#window.bind('<KeyPress>', lambda event: print('button was pressed:',event)) # triggered when any key is pressed

entry.bind('<FocusIn>', lambda event: print('entry field was selected'))
entry.bind('<FocusOut>', lambda event: print('entry field was unselected'))

#exercise
text.bind('<Shift-MouseWheel>', lambda event: print('Mousewheel'))

#run
window.mainloop()