from tkinter import *
root = Tk()

e = Entry(root)
e.pack()
def func ():
    myLabel = Label(root, text="clicked")
    myLabel.pack()

myButton = Button(root, text='click me', padx= 50, pady = 20, command=func, bg='#fff', fg='#000')
myButton.pack()

root.mainloop()