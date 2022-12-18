from tkinter import messagebox
from tkinter import *


def Exit():
    Answer = messagebox.askquestion("Exit Confirm", "Are you sure you want to close the program?")
    if Answer == "yes":
        root.destroy()

def Prime():
    try:
        MainNumber = Variable.get()
        if MainNumber >= 0:
            if MainNumber != 1 and MainNumber != 0:
                Number2 = MainNumber - 1
                while Number2 != 1:
                    if MainNumber % Number2 == 0:
                        Label(root, text=f"         " * 16, bg="#053f5c", fg="#053f5c", font=('Times New Roman', 22)).place(x=280, y=350)
                        Label(root, text=f"Number {MainNumber} isn't prime.", bg="#053f5c", fg="#9fe7f5", font=('Times New Roman', 22)).place(x=280, y=350)
                        break
                    Number2 -= 1
                if Number2 == 1:
                    Label(root, text=f"         " * 16, bg="#053f5c", fg="#053f5c", font=('Times New Roman', 22)).place(x=280, y=350)
                    Label(root, text=f"Number {MainNumber} is prime.", bg="#053f5c", fg="#9fe7f5", font=('Times New Roman', 22)).place(x=280, y=350)
            else:
                Label(root, text=f"         " * 16, bg="#053f5c", fg="#053f5c", font=('Times New Roman', 22)).place(x=280, y=350)
                Label(root, text=f"Number {MainNumber} isn't prime.", bg="#053f5c", fg="#9fe7f5", font=('Times New Roman', 22)).place(x=280, y=350)
        else:
            Label(root, text=f"         " * 16, bg="#053f5c", fg="#053f5c", font=('Times New Roman', 22)).place(x=280, y=350)
            Label(root, text=f"Your number must not be negative", bg="#053f5c", fg="#9fe7f5", font=('Times New Roman', 22)).place(x=280, y=350)
    except:
        messagebox.showerror("Invalid value", "Your number must be integer or decimal")


root = Tk()
title = root.title("Prime Number")
root.configure(bg='#053f5c')
root.geometry('800x450+540+270')
root.resizable(width=False, height=False)

Variable = IntVar()
Titre = Label(root, text="Prime Number", bg="#053f5c", fg="#F7AD19", font=('Times New Roman', 30)).place(x=280, y=25)
MainNumber = Entry(root, bg="#fbc316", width=20, textvariable=Variable).place(x=570, y=145)
text1 = Label(root, text="Please enter the number: ", bg="#053f5c", fg="#9fe7f5", font=('Times New Roman', 24)).place(x=110, y=145)
Button = Button(root, text="Calculate", bg="#f8880a", fg="#9fe7f5", font=('Times New Roman', 14), width=10, command=Prime).place(x=577, y=210)

Menubar = Menu(root, bg="#053f5c", fg="#053f5c")
exit = Menu(Menubar, bg="#053f5c", fg="#fbc316", tearoff=0)
exit.add_command(label="Exit", command=Exit)
Menubar.add_cascade(label="Exit", menu=exit)
root.config(menu=Menubar)
root.mainloop()
