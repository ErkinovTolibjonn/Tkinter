from tkinter import *

parent = Tk()

name = Label(parent,text='Name').place(x = 10,y=50)

email = Label(parent,text="Email").place(x=10,y=90)

password = Label(parent,text='Password').place(x=10,y=130)

submit = Button(parent,text="Submit").place(x=10,y=170)

e_name = Entry(parent).place(x=80,y=50)

e_email = Entry(parent).place(x=80,y=90)

e_password = Entry(parent).place(x=95,y=130)


parent.mainloop()