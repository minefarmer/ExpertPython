from tkinter import *

def onButtonPress():
    labelVariable.set('welcome')
    
# main window
root = Tk()

labelVariable = StringVar() # string variable
# textvariable associates a Tkinter variable (usually a Sreingvar) with the label.
# If the variable is changed, the label text is updated. 
l = Label(root,textvariable=labelVariable, anchor="w",fg="white",bg='blue')
# initialize the variable
labelVariable.set("Hello !")
l.grid(column=0,row=0)

button =Button(root,text = 'click' ,command=onButtonPress)
button.grid(column=1,row=0)

root.mainloop()
