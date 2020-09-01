from tkinter import  *
from tk_class import Hello 

parent = Frame(None)
parent.pack()
Hello(parent).pack()

Button(parent,text='clickme',command = exit , fg = 'white' ,bg = 'black').pack(side=RIGHT)
parent.mainloop()

