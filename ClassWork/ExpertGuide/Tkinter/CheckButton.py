from tkinter import *

top = Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()

# the control VARIABLE tracks the current state of the checkbutton.Normally this variable is an IntVar, and 0 means cleared and 1 means set, but I can change these values using the onvalue and offvalue options.

C1 = Checkbutton(top, text= "Music", variable = CheckVar1, onvalue = 1, offvalue = 0)
C2 = Checkbutton(top, text = "Video", variable = CheckVar2, onvalue = 1, offvalue = 0)
print(CheckVar1.get());
C1.pack()
C2.pack()
top.mainloop()
