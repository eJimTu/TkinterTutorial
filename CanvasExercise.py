import tkinter as tk

window = tk.Tk()
window.geometry('600x400')
window.title('Canvas')

def drawLine (event):
    x = event.x
    y = event.y
    canvas.create_oval((x-brushSize*0.5, y-brushSize*0.5, x+brushSize*0.5, y+brushSize*0.5), fill='black')

def brushSizeAdjust(event):
    global brushSize 

    if event.delta > 0:
        brushSize += 1
    else:
        brushSize -= 1

    brushSize = max(0,min(brushSize,50))    

#canvas widget
Pos_x = tk.IntVar(value = 0)
Pos_y = tk.IntVar(value = 0)
canvas = tk.Canvas(window, bg = 'white')
canvas.pack()
#exercise bind event to create paint app

brushSize = 4
canvas.bind('<Alt-Motion>', drawLine)
canvas.bind('<MouseWheel>', brushSizeAdjust)
#canvas.create_rectangle((50,20,100,200), fill = 'red', width = 5, dash = (1,2), outline = 'blue') #(left, top, right, bottom) from the edges of the side
#canvas.create_line(0,0, 100, 150)

window.mainloop()