import tkinter
canvas=tkinter.Canvas()

#canvas.create_line(10, 100, 140, 100, 140, 150, 10, 150,10, 100,
#                    width = 2, fill = 'red')
#moj prikaz
canvas.create_rectangle(10, 100, 140, 150, width = 2,
                        fill = 'yellow', outline = 'yellow' )
canvas.create_rectangle(140, 100, 270, 150, width = 2,
                        fill = 'red', outline = 'red' )
canvas.create_rectangle(10, 150, 140, 200, width = 2,
                        fill = 'green', outline = 'green' )
canvas.pack()
