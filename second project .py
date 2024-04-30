from tkinter import*
root  = Tk()


fm = Frame(root)
fm.pack(fill=BOTH)
Button(fm,text="Button1",fg="orange").pack()
Button(fm,text="Button2",fg="black").pack(side=RIGHT)
Button(fm,text="Button3",fg="green").pack(side=LEFT)
root.mainloop()