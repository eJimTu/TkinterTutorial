import tkinter as tk
from tkinter import ttk
from random import choice

window = tk.Tk()
window.geometry('600x400')
window.title('Treeview')

firstName = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Anna', 'Lisa']
lastName = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']

#treeview

table = ttk.Treeview(window, columns = ('first', 'last', 'email'), show='headings')
table.heading('first', text='First name')
table.heading('last', text='Surname')
table.heading('email', text='Email')
table.pack(fill='both', expand= True)

#insert value into table
for i in range(100):
    first = choice(firstName)
    last = choice(lastName)
    email = first + "@email.com"
    table.insert(parent='', index=i, values=(first, last, email))

table.insert(parent='', index= tk.END, values=('XXXX', 'YYYYY', 'ZZZZ'))

#events

def itemSelect(_):
    print(table.selection())
    
    for i in table.selection():
        print(table.item(i)['values'])
    #table.item(table.selection())

def deleteItems(_):
    
    for i in table.selection():
        table.delete(i)

table.bind('<<TreeviewSelect>>', itemSelect)
table.bind('<Delete>', deleteItems)
#items

window.mainloop()