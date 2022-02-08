import tkinter
canvas = tkinter.Canvas()
canvas.pack()

def kruzok(suradnice):
    x = suradnice.x
    y = suradnice.y
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5)

def stvorec(suradnice):
    x = suradnice.x
    y = suradnice.y
    canvas.create_rectangle(x - 5, y - 5, x + 5, y + 5)

canvas.bind('<Button-1>', kruzok)
canvas.bind('<Button-3>', stvorec)
