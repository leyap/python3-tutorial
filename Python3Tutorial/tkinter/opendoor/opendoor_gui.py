from tkinter import *
import requests

root = Tk()
def opendoor():
	requests.get("http://10.0.10.10/command?cmd=open")
button = Button(root, text="open", command=opendoor)
button.pack()
root.mainloop()

