import tkinter
from tkinter import *


d=''
s=''


def onclick():
    global d
    global s
    d=str(e2.get())
    s=str(e1.get())
    window.destroy()
    

window = tkinter.Tk()
window.configure(background="#a1dbcd")

window.title("AmazonWebCrawler")


photo = tkinter.PhotoImage(file="a2.ppm")
w = tkinter.Label(window, image=photo)
w.pack()


lblInst = tkinter.Label(window, text="Please Fill to continue:", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 16))

lblInst.pack()

l1 = tkinter.Label(window, text="Search_Here:", fg="#383a39", bg="#a1dbcd")
e1 = tkinter.Entry(window)

l1.pack()
e1.pack()


l2 = tkinter.Label(window, text="File_Location:", fg="#383a39", bg="#a1dbcd")
v=StringVar()
v.set('/home/anany/Downloads/')
e2 = tkinter.Entry(window,textvariable=v)
l2.pack()

e2.pack()


btn = tkinter.Button(window, text="Start", fg="#a1dbcd", bg="#383a39",command=onclick)

btn.pack()


window.mainloop()
