import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import ttk


def click(event):
    print("Button clicked")

root = tk.Tk()

root.title("My app")
root.geometry("400x300")

# label = tk.Label(root, text="Hello World")
# label.pack()

# label1 = tk.Label(root,text="heheheheheheehheheheheh")
# label1.pack()

# button = tk.Button(root,text="click me",command=click)
# button = tk.Button(
#     root,
#     text="Click",
#     bg="black",
#     fg="white",
#     font=("Arial", 14)
# )
# button.pack()

# entry = tk.Entry(root)
# entry.pack()
# text = entry.get()

# tk.Label(root, text="Name").grid(row=0, column=0)
# tk.Entry(root).grid(row=0, column=1)

# frame = tk.Frame(root)
# frame.pack()

# tk.Button(frame, text="Button1").pack()
# root.bind("<Button-1>", click)
# tk.Button(frame, text="Button2").pack()

# messagebox.showinfo("Title", "Message")
# messagebox.showwarning("Title", "Message")
# messagebox.showerror("Title", "Message")
# messagebox.askyesno("Title", "Message")

# menu = tk.Menu(root)
# root.config(menu=menu)

# file = tk.Menu(menu)
# fil = tk.Menu(menu)

# menu.add_cascade(label="File", menu=file)
# menu.add_cascade(label="text", menu=fil)


# file.add_command(label="Open")
# file.add_command(label="Exit")

# fil.add_command(label="ee")
# fil.add_command(label="ee")

# img = PhotoImage(file="image.png")
# label = Label(root, image=img)
# label.pack()

# button = ttk.Button(root, text="Modern Button")
# button.pack()

# root.mainloop()












# calulator type
# import tkinter as tk

# def add():
#     result = int(e1.get()) + int(e2.get())
#     label.config(text=result)

# def sub():
#     result = int(e1.get()) - int(e2.get())
#     label.config(text=result)

# def mul():
#     result = int(e1.get()) * int(e2.get())
#     label.config(text=result)

# def div():
#     result = int(e1.get()) / int(e2.get())
#     label.config(text=result)



# root = tk.Tk()

# e1 = tk.Entry(root)
# e1.pack()

# e2 = tk.Entry(root)
# e2.pack()

# btn = tk.Button(root, text="Add", command=add)
# btn.pack()
# btn = tk.Button(root, text="subtract", command=sub)
# btn.pack()
# btn = tk.Button(root, text="multiply", command=mul)
# btn.pack()
# btn = tk.Button(root, text="divide", command=div)
# btn.pack()

# label = tk.Label(root, text="Result")
# label.pack()

# root.mainloop()


#login form

import tkinter as tk

def login():
    print(username.get(), password.get())

root = tk.Tk()

tk.Label(root, text="Username").pack()
username = tk.Entry(root)
username.pack()

tk.Label(root, text="Password").pack()
password = tk.Entry(root, show="*")
password.pack()

tk.Button(root, text="Login", command=login).pack()

root.mainloop()
