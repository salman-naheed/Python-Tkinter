from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Hi')

frame = LabelFrame(root, text='Frame', padx= 10,pady=10)
frame.pack(padx=10, pady=10)
b = Button(frame, text='Click')
b.pack()
root.mainloop()