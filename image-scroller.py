from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title('App')
root.iconbitmap('C:/Users/CallMeSalman/Pictures/icon.ico')

my_img = ImageTk.PhotoImage(Image.open("C:/Users/CallMeSalman/Pictures/SAL.png")) #add ur own directory
my_label = Label(image=my_img, width=300, height=300)
my_label.pack()


quit = Button(root, text='Quit', command=root.quit)
quit.pack()






root.mainloop()