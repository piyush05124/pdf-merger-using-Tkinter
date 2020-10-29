from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
from PyPDF2 import PdfFileMerger
merger = PdfFileMerger()


root = Tk()
root.geometry("900x750")
root.resizable(width=True, height=True)
li=[]

def openfn():
    index=1
    filename = filedialog.askopenfilename(title='op')
    Lb1.insert(index,filename)
    index+=1
    li.append(filename)
    return li

def cat():
    for i in li:
        merger.append(i)
    tt=E1.get()
    merger.write("{}.pdf".format(tt))
    merger.close()    
        
    

btn = Button(root, text='open PDF', command=openfn,bd=5).pack(side=LEFT,padx=40,ipadx=20, ipady=10 )
save = Button(root, text='Merge PDF', command=cat,bd=6).pack(side=BOTTOM,padx=0,pady=40,ipadx=20, ipady=10)
L1 = Label(root, text="Save As")
L1.pack( side = LEFT)

E1 = Entry(root, bd =15)
E1.pack(side = LEFT,ipadx=20)

Lb1 = Listbox(root,bd=20)
Lb1.pack(expand=True,ipadx=40)
##root.mainloop()
