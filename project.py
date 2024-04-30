from tkinter import*
root=Tk()
root.geometry("500x400")
root.title("This is my first GUI")
Label=Label(text="Ready",padx=50,pady=70,relief=GROOVE,bg="Red",fg="yellow",border=90,font="italic20bold")
Label.pack(fill=Y,anchor="center",padx=200,pady=100)

root.mainloop()

