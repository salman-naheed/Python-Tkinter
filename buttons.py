from tkinter import *
root = Tk()

def func ():
    myLabel = Label(root, text="clicked")
    myLabel.pack()

myButton = Button(root, text='click me', padx= 50, pady = 20, command=func, bg='#000', fg='#fff')
myButton.pack()

root.mainloop()