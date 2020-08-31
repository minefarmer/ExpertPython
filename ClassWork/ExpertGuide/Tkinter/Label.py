from tkinter import *
root = Tk()
label = Label(root, text = 'Python is fun')

# yellow text on black label
label.config(fg='yellow',bg='green')

# use larger font
label.config(font=('times',40,'bold'))

# shape of cursor are: cross,pirate'hand2.watch
label.config(cursor = 'cross')

# initial size:lines,chars . border width and style
label.config(height = 3, width=20,bd=18,relief = GROOVE)

# add empty space around the widget
label.pack(padx=20,pady=20, expand = YES,fill =BOTH)
root.mainloop()
