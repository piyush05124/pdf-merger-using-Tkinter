
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

root = Tk()
root.geometry("550x300+300+150")
root.resizable(width=True, height=True)

def openfn():
    filename = filedialog.askopenfilename(title='op')
    return filename
def open_img():
    
    x = openfn()
    img = Image.open(x)
    #img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    Label(root,text=" ") 
    panel.pack()


def go():
      return sys.exit(1)
btn = Button(root, text='open image', command=open_img).pack()
btn2= Button(root, text='exit', command=go).pack()

root.mainloop()
