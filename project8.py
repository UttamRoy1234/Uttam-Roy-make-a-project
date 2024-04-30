from tkinter import*
from PIL import Image,ImageTk
root=Tk()
root.geometry("1200x900")
#photo=PhotoImage(file="1.png")


image=Image.open("photo.jpg")
photo =ImageTk.PhotoImage(image)

Label=Label(image=photo).pack()





root.mainloop()