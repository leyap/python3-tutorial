from tkinter import *

def processButton():
	print("you click button")

window = Tk()
label = Label(window, text="welcome to Python")
button = Button(window, text = "Click Me", bg="Yellow", command=processButton)
label.pack()
button.pack()

window.mainloop()
