import tkinter as tk
from tkinter import *
import os
import getpass
from datetime import date, datetime
from OpenZCS.zcs import *
from OpenZCS import ZSFS

# date
def date():
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")
    return date_time

# host username
username = getpass.getuser()

def run():
    INPUT = input.get("1.0", "end-1c")
    console.config(state="normal")
    set_string = tk.StringVar() # Create the variable 
    set_string.set(INPUT)
    if 'Print("' in INPUT:
        console.delete('1.0', END)
        OUTPUT = Print(INPUT)
        date_time = date()
        console.insert(END, ''+(date_time)+' - '+(OUTPUT)+''+'\n')
        console.insert(END, ''+(date_time)+' - Program ran successfully.'+'\n')
        console.config(state=DISABLED)
    if 'MsgBox("' in INPUT:
        console.delete('1.0', END)
        MsgBox(INPUT)
        date_time = date()
        console.insert(END, ''+(date_time)+' - Program ran successfully.'+'\n')
        console.config(state=DISABLED)
    else:
        console.delete('1.0', END)
        console.insert(END, ""+'\n')
        console.config(state=DISABLED)

def about():
   about = Toplevel()
   about.title("About (OpenZCS) (debug)")
   p2 = PhotoImage(file = 'OpenZCS/about.png')
   about.iconphoto(False, p2)
   about.geometry("450x550")
   about.minsize(450, 550)
   about.maxsize(450, 550)
   about.configure(bg='white')
   def exit_about():
        about.destroy()
        about.update()
   Label(about, text = "zeqOS", bg="white", font =('Segoe UI Semibold', 28)).place(x=75, y=45)
   Label(about, text = "Chabazite", bg="white", font =('Segoe UI Light', 28)).place(x=195, y=45)
   Label(about, text = "OpenZCS", bg="white", font =('Segoe UI Light', 10)).place(x=350, y=45)
   Button(master=about, borderwidth=0, bg='black', fg='white', text="OK", relief="flat", width=7, height=1, command=lambda:exit_about(), font=('Segoe UI Semibold', 10)).place(x=383, y=517)
   Label(about, text = "zeqOS Studio (OpenZCS) - Version 1.0.1 Chabazite", bg="white", font =('Segoe UI', 8)).place(x=20, y=135)
   Label(about, text = """The zeqOS Chabazite Series is produced and owned by Zulo. Do not share or 
view code.""", bg="white", justify=LEFT, font  =('Segoe UI', 8)).place(x=20, y=155)
   Label(about, text = """This product was licensed to: 
"""+(username)+"""""", bg="white", justify=LEFT, font  =('Segoe UI', 8)).place(x=20, y=445)


window = Tk(className='zeqOS Studio (OpenZCS) (debug)')
img = PhotoImage(file="OpenZCS/OK_Button.png")
# set window size
window.geometry("900x600")
window.configure(bg='white')
Button(master=window, text="New", relief="flat", width=5, height=1, font=('Segoe UI Semibold', 11), bg="white").place(x=5, y=0)
Button(master=window, text="Save", relief="flat", width=5, height=1, font=('Segoe UI Semibold', 11), bg="white").place(x=60, y=0)
Button(master=window, text="Run", relief="flat", width=5, height=1, font=('Segoe UI Semibold', 11), bg="white", command = lambda:run()).place(x=115, y=0)
Button(master=window, text="Help", relief="flat", width=5, height=1, font=('Segoe UI Semibold', 11), bg="white").place(x=170, y=0)
Button(master=window, text="Info", relief="flat", width=5, height=1, font=('Segoe UI Semibold', 11), bg="white", command = lambda:about()).place(x=225, y=0)
Label(window, text = "Project Code", bg="white", font =('Segoe UI Semibold', 11)).place(x=15, y=45)
input = Text(window, height = 15, width = 108, relief="flat",font =('Segoe UI', 11), bg = "white")
input.place(x=15, y=75)
input.insert(END, '<Project1 : Application ZCS>'+'\n')
input.insert(END, ''+'\n')
input.insert(END, '</Project1>')


Label(window, text = "Console View", bg="white", font =('Segoe UI Semibold', 11)).place(x=15, y=385)
console = Text(window, height = 8, width = 108, relief="flat",font =('Segoe UI', 10), bg = "white")
console.place(x=15, y=415)
date_time = date()
console.insert(END, ''+(date_time)+' - '+(username)+' just created their own ZCS Project.'+'\n')
console.config(state=DISABLED)

p1 = PhotoImage(file = 'OpenZCS/zeqosstudio.png')
 
# Setting icon of master window
window.iconphoto(False, p1)
window.mainloop()