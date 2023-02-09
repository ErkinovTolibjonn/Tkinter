from tkinter import *
from tkinter import messagebox

parent = Tk()

parent.geometry('200x200')

def func():
    messagebox.showinfo('hello',)

but1 = Button(parent,text='Red',command=func,foreground='red',background='pink',pady=10)
but1.pack(side=RIGHT)

but2 = Button(parent,text='Blue',command=func,foreground='blue',background='pink',pady=10)
but2.pack(side=TOP)

but3 = Button(parent,text='Green',command=func,foreground='green',background='pink',pady=10)
but3.pack(side=BOTTOM)

but4 = Button(parent,text='Cyan',command=func,foreground='cyan',background='pink',pady=10)
but4.pack(side=LEFT)

parent.mainloop()