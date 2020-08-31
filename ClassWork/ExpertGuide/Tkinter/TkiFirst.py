# import the module Tkinter
from tkinter import *

master = Tk()

w = Scale(master, from_=0, to=100)
w.pack()
print(w.get())
w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
w.pack()
print(w.get())
mainloop()










# # create the GUI application main window
# root = Tk( )
# root.title("A simple application")

# # Add one or more widgets to the GUI application.
# label=Label(root,text='hello world!!')

# # pack the label in the parent widget.
# label.pack()

# # Adding s button and packing it in the same statement.
# Button(root,text='click', command= exit).pack()

# # Calls the mainloop to bring up the window and start the tkinter event loop.
# root.mainloop()
