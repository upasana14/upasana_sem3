# from email import message
from tkinter import *
from tkinter import  messagebox

w=Tk()

w.geometry("300x100")

def fun():
    messagebox.showinfo("Hello","Red button clicked")
btn=Button(w,text="Red",command=fun,activeforeground="yellow", activebackground="pink",pady=10)
btn.pack(side=LEFT)

b1=Button(w,text="Click me !")
b1.pack(fill=X,expand=True)

b2=Button(w,text="Click me too")
b2.pack(fill=Y,expand=True)


w.mainloop()