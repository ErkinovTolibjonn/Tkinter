from tkinter import *

parent = Tk()

redbut = Button(parent,text='Red',fg='red')
redbut.pack(side='top')

cyanbut = Button(parent,text='Cyan',fg='cyan')
cyanbut.pack(side='right')

blackbut = Button(parent,text='Black',fg='black')
blackbut.pack(side='left')

greenbut = Button(parent,text='Green',fg='green')
greenbut.pack(side='bottom')

parent.mainloop()