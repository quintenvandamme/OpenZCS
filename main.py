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

def new():
   input.delete('1.0', END)
   input.insert(END, '<Project1 : Application ZCS>'+'\n')
   input.insert(END, ''+'\n')
   input.insert(END, '</Project1>')
   console.config(state="normal")
   console.delete('1.0', END)
   date_time = date()
   console.insert(END, ''+(date_time)+' - '+(username)+' just created their own ZCS Project.'+'\n')
   console.config(state=DISABLED)

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
   Label(about, text = "zeqOS", bg="white", fg='black', highlightbackground = "white", font =('Segoe UI Semibold', 28)).place(x=75, y=45)
   Label(about, text = "Chabazite", bg="white", fg='black', highlightbackground = "white", font =('Segoe UI Light', 28)).place(x=195, y=45)
   Label(about, text = "OpenZCS", bg="white", fg='black', highlightbackground = "white", font =('Segoe UI Light', 10)).place(x=350, y=45)
   Button(master=about, borderwidth=0, bg='black', fg='white', highlightbackground = "white", text="OK", relief="flat", width=7, height=1, command=lambda:exit_about(), font=('Segoe UI Semibold', 10)).place(x=383, y=517)
   Label(about, text = "zeqOS Studio (OpenZCS) - Version 1.0.1 Chabazite", bg="white", fg='black', highlightbackground = "white", font =('Segoe UI', 8)).place(x=20, y=135)
   Label(about, text = """The zeqOS Chabazite Series is produced and owned by Zulo. Do not share or 
view code.""", bg="white", fg='black', highlightbackground = "white", justify=LEFT, font  =('Segoe UI', 8)).place(x=20, y=155)
   Label(about, text = """This product was licensed to: 
"""+(username)+"""""", bg="white", fg='black', highlightbackground = "white", justify=LEFT, font  =('Segoe UI', 8)).place(x=20, y=445)

def help():
   help = Toplevel()
   help.title("Help (OpenZCS) (debug)")
   p3 = PhotoImage(file = 'OpenZCS/help.png')
   help.iconphoto(False, p3)
   help.geometry("450x550")
   help.minsize(450, 550)
   help.maxsize(450, 550)
   help.configure(bg='white')
   Button(master=help, borderwidth=0, bg='black', fg='white', highlightbackground = "black", text="OK", relief="flat", width=7, height=1, command=lambda:help_exit(help), font=('Segoe UI Semibold', 10)).place(x=383, y=517)
   helpN = Button(master=help, borderwidth=0, bg='black', fg='white', highlightbackground = "black", text="Next", relief="flat", width=7, height=1, command=lambda:help_next(), font=('Segoe UI Semibold', 10))
   helpN.place(x=300, y=517)
   helpB = Button(master=help, borderwidth=0, bg='grey', fg='white', highlightbackground = "black", text="Back", relief="flat", width=7, height=1, command=lambda:help_back(), font=('Segoe UI Semibold', 10))
   helpB.place(x=225, y=517)
   help_view = Text(help, height = 28, width = 60, fg='black', highlightbackground = "white", relief="flat",font =('Segoe UI', 10), bg = "white")
   help_view.place(x=15, y=10)
   help_view.insert(END, 'zeqOS Studio -Page 1-'+'\n'+''+'\n'+'Thanks for checking out the help page! By browsing this guide,'+'\n'+'you will learn how to use zeqOS Studio and how to code'+'\n'+'applications ready for the zeqOS Store in ZCS.'+'\n')
   help_view.config(state=DISABLED)

   def help_exit(help_page):
      help_page.destroy()
      help_page.update()

   def help_next():
      INPUT = help_view.get("1.0", "end-1c")
      help_view.config(state="normal")
      set_string = tk.StringVar() # Create the variable 
      set_string.set(INPUT)
      if 'zeqOS Studio -Page 1-' in INPUT:
         helpstr1 = "What does that mean? You have to say if it's a string, or an"
         helpstr2 = "Note: Integer Variables aren't fully supported right now."
         help_view.delete('1.0', END)
         help_view.insert(END, 'ZCS Functions -Page 2-'+'\n'+''+'\n'+'To store a variable(to create one), you first have to declare it.'+'\n'+(helpstr1)+'\n'+'integer(a number)'+'\n'+(helpstr2)+'\n'+''+'\n'+'Let VariableName be String'+'\n'+'Set VariableName as "Hello"'+'\n'+''+'\n'+'VariableName can be set as anything. "Hello" is the value of the'+'\n'+'variable, so you can put whatever you want in it.'+'\n'+'ZCS has functions, too!'+'\n'+'Currently, there are just 4 of them:(one of them is a value'+'\n'+'function)'+'\n'+''+'\n'+'-Print Print("hello")'+'\n'+'You can use Print to show stuff in the Console View in the zeqOS'+'\n'+'Studio. You can use a string variable if you want.'+'\n'+''+'\n'+'-MsgBox MsgBox("hi")'+'\n'+'You can use MsgBox, just like you would in VBA. It shows up the'+'\n'+'Windows MsgBox dialog. Write anything you want.'+'\n')
         help_view.config(state=DISABLED)
         helpB.config(bg="black")
      if 'ZCS Functions -Page 2-' in INPUT:
         helpstr3 = "-Comments 'Hello Any line starting with a ' will get ignored. Say"
         help_view.delete('1.0', END)
         help_view.insert(END, 'ZCS Functions -Page 3-'+'\n'+''+'\n'+'-MessageBox MessageBox("title","description") You can use'+'\n'+'MessageBox just like you would would in Windows, but this one'+'\n'+'shows up in zeqOS and has a title and description.'+'\n'+''+'\n'+(helpstr3)+'\n'+'anything that you want in here. -Rnd(Min, Max) Print(Rnd(1,10))'+'\n'+'Random number generator. Min is the minimum value, Max is the'+'\n'+'maximum value.'+'\n')
         help_view.config(state=DISABLED)
         helpN.config(bg="grey")          

   def help_back():
      INPUT = help_view.get("1.0", "end-1c")
      help_view.config(state="normal")
      set_string = tk.StringVar() # Create the variable 
      set_string.set(INPUT)
      if 'ZCS Functions -Page 2-' in INPUT:
         help_view.delete('1.0', END)
         help_view.insert(END, 'zeqOS Studio -Page 1-'+'\n'+''+'\n'+'Thanks for checking out the help page! By browsing this guide,'+'\n'+'you will learn how to use zeqOS Studio and how to code'+'\n'+'applications ready for the zeqOS Store in ZCS.'+'\n')
         help_view.config(state=DISABLED)
         helpB.config(bg="grey")
         helpN.config(bg="black")          
      if 'ZCS Functions -Page 3-' in INPUT:
         helpstr1 = "What does that mean? You have to say if it's a string, or an"
         helpstr2 = "Note: Integer Variables aren't fully supported right now."
         help_view.delete('1.0', END)
         help_view.insert(END, 'ZCS Functions -Page 2-'+'\n'+''+'\n'+'To store a variable(to create one), you first have to declare it.'+'\n'+(helpstr1)+'\n'+'integer(a number)'+'\n'+(helpstr2)+'\n'+''+'\n'+'Let VariableName be String'+'\n'+'Set VariableName as "Hello"'+'\n'+''+'\n'+'VariableName can be set as anything. "Hello" is the value of the'+'\n'+'variable, so you can put whatever you want in it.'+'\n'+'ZCS has functions, too!'+'\n'+'Currently, there are just 4 of them:(one of them is a value'+'\n'+'function)'+'\n'+''+'\n'+'-Print Print("hello")'+'\n'+'You can use Print to show stuff in the Console View in the zeqOS'+'\n'+'Studio. You can use a string variable if you want.'+'\n'+''+'\n'+'-MsgBox MsgBox("hi")'+'\n'+'You can use MsgBox, just like you would in VBA. It shows up the'+'\n'+'Windows MsgBox dialog. Write anything you want.'+'\n')
         help_view.config(state=DISABLED)
         helpN.config(bg="black")          

window = Tk(className='zeqOS Studio (OpenZCS) (debug)')
img = PhotoImage(file="OpenZCS/OK_Button.png")
# set window size
window.geometry("900x600")
window.configure(bg='white')
Button(master=window, text="New", relief="flat",borderwidth=0, width=5, height=1, font=('Segoe UI Semibold', 11), fg="black", highlightbackground = "white", bg="white", command = lambda:new()).place(x=5, y=0)
Button(master=window, text="Save", relief="flat",borderwidth=0, width=5, height=1, font=('Segoe UI Semibold', 11), fg="black", highlightbackground = "white", bg="white").place(x=60, y=0)
Button(master=window, text="Run", relief="flat",borderwidth=0, width=5, height=1, font=('Segoe UI Semibold', 11), fg="black", highlightbackground = "white", bg="white", command = lambda:run()).place(x=115, y=0)
Button(master=window, text="Help", relief="flat",borderwidth=0, width=5, height=1, font=('Segoe UI Semibold', 11), fg="black", highlightbackground = "white", bg="white", command = lambda:help()).place(x=170, y=0)
Button(master=window, text="Info", relief="flat",borderwidth=0, width=5, height=1, font=('Segoe UI Semibold', 11), fg="black", highlightbackground = "white", bg="white", command = lambda:about()).place(x=225, y=0)
Label(window, text = "Project Code", fg="black", highlightbackground = "white", bg="white", font =('Segoe UI Semibold', 11)).place(x=15, y=45)
input = Text(window, height = 15, width = 108, fg="black", highlightbackground = "white", relief="flat",font =('Segoe UI', 11), bg = "white")
input.place(x=15, y=75)
input.insert(END, '<Project1 : Application ZCS>'+'\n')
input.insert(END, ''+'\n')
input.insert(END, '</Project1>')


Label(window, text = "Console View", bg="white", fg="black", highlightbackground = "white", font =('Segoe UI Semibold', 11)).place(x=15, y=385)
console = Text(window, height = 8, width = 108, fg="black", highlightbackground = "white", relief="flat",font =('Segoe UI', 10), bg = "white")
console.place(x=15, y=415)
date_time = date()
console.insert(END, ''+(date_time)+' - '+(username)+' just created their own ZCS Project.'+'\n')
console.config(state=DISABLED)

p1 = PhotoImage(file = 'OpenZCS/zeqosstudio.png')
 
# Setting icon of master window
window.iconphoto(False, p1)
window.mainloop()
