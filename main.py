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
        INPUT = INPUT.replace('<Project1 : Application ZCS>', '')
        INPUT = INPUT.replace('</Project1>', '')
        INPUT = INPUT.replace('Print("', '')
        INPUT = INPUT.replace('")', '')
        OUTPUT = INPUT.strip()
        date_time = date()
        console.insert(END, ''+(date_time)+' - '+(OUTPUT)+''+'\n')
        console.insert(END, ''+(date_time)+' - Program ran successfully.'+'\n')
        console.config(state=DISABLED)
    else:
        console.insert(END, ""+'\n')
        console.config(state=DISABLED)

def info():
   window = Toplevel() # className='About (OpenZCS) (debug)'
   #window = Tk() 
   window.title("About (OpenZCS) (debug)")
   window.geometry("450x550")
   window.minsize(450, 550)
   window.maxsize(450, 550)
   window.configure(bg='white')
   Label(window, text = "zeqOS", bg="white", font =('Segoe UI Semibold', 28)).place(x=75, y=45)
   Label(window, text = "Chabazite", bg="white", font =('Segoe UI Light', 28)).place(x=195, y=45)
   Label(window, text = "OpenZCS", bg="white", font =('Segoe UI Light', 10)).place(x=350, y=45)
   Button(master=window, borderwidth=0, text="OK", relief="flat", width=4, height=1, font=('Segoe UI Semibold', 11)).place(x=300, y=470)


window = Tk(className='zeqOS Studio (OpenZCS) (debug)')
img = PhotoImage(file="OK_Button.png")
# set window size
window.geometry("900x600")
window.configure(bg='white')
Button(master=window, text="New", relief="flat", width=5, height=1, font=('Segoe UI Semibold', 11), bg="white").place(x=5, y=0)
Button(master=window, text="Save", relief="flat", width=5, height=1, font=('Segoe UI Semibold', 11), bg="white").place(x=60, y=0)
Button(master=window, text="Run", relief="flat", width=5, height=1, font=('Segoe UI Semibold', 11), bg="white", command = lambda:run()).place(x=115, y=0)
Button(master=window, text="Help", relief="flat", width=5, height=1, font=('Segoe UI Semibold', 11), bg="white").place(x=170, y=0)
Button(master=window, text="Info", relief="flat", width=5, height=1, font=('Segoe UI Semibold', 11), bg="white", command = lambda:info()).place(x=225, y=0)
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

p1 = PhotoImage(file = 'zeqosstudio.png')
 
# Setting icon of master window
window.iconphoto(False, p1)
window.mainloop()