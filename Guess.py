from tkinter import *
import tkinter.messagebox
import random
import math

screen=Tk()
screen.minsize(350,250)
screen.title("Guess The Number")
cn=random.randint(1,20)

def greet():
    nf=nent.get()
    tkinter.messagebox.showinfo("name","Well "+nf+" i'm thinking of a number between 1-20")
    
def guess1():
    gf=tent.get() 
    gf=int(gf)
    if gf>cn:
       tkinter.messagebox.showinfo("High","Your guess is too high")
    elif gf<cn:
        tkinter.messagebox.showinfo("Low","Your guess is too low")
    elif gf==cn:
        tkinter.messagebox.showinfo("Correct","Your guess is correct!")
    else:
        tkinter.messagebox.showinfo("Invalid input","Give a number between 1-20")
    
wel=Label(screen,text="Welcome to the game!")
wel.pack()

name=Label(screen,text="What's your name?")
name.place(x=10,y=50)
nent=Entry(screen,width=20)
nent.place(x=10,y=70)
ok=Button(screen,text="OK",command=greet)
ok.place(x=200,y=65)

take=Label(screen,text="Take a guess")
take.place(x=10,y=150)
tent=Entry(screen,width=20)
tent.place(x=10,y=170)
guess=Button(screen,text="Guess",command=guess1)
guess.place(x=200,y=165)

screen.mainloop()
