from tkinter import*
root =Tk()
Label__1=Label(root,text="Username")
Label__2=Label(root,text="Password")

Label__1.grid(row=0)
Label__2.grid(row=1)


entry__1 =Entry(root)
entry__2 =Entry(root)


entry__1.grid(row=0,column=1)
entry__2.grid(row=1,column=1)

root.mainloop()