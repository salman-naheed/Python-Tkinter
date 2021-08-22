from tkinter import *

root = Tk()

# Creating label widget
myLabel = Label(root, text="Hello")
myLabel1 = Label(root, text="Hello")

# grids
myLabel.grid(row=0, column=0)
myLabel1.grid(row=1, column=0)

root.mainloop()
