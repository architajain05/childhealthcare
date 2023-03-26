from tkinter import *
from tkinter import messagebox
import sqlite3
import os


root=Tk()

photo=PhotoImage(file="C:\\Users\\DELL\\Desktop\\600.png")
l=Label(root)
l.configure(image=photo)
l.place(x=0,y=110)

root.geometry("700x500")
root.title("Login Screen")
root.configure(bg="white")
root.attributes("-fullscreen",True)
txtusername=StringVar()
txtpassword=StringVar()

def createuser_clicked():
    import createuser

def login_clicked():
    con=sqlite3.connect("inventory.sqlite")
    c=con.cursor()
    u=txtusername.get()
    p=txtpassword.get()
    c.execute("select * from user where username=? and password=?",(u,p))
    data=c.fetchall()
    if len(data)==0:
        messagebox.showinfo("Alert!","Username/Password does not exit")
    else:
        messagebox.showinfo("Great!","Login Successful..")
      
def clear_clicked():
    txtusername.set("")
    txtpassword.set("")

def exit_clicked():
    root.destroy()

l0=Label(root,text="LOGIN SCREEN",width="17",bg="black",fg="white",font=("Lucida Handwriting",50,"bold"))
l0.place(x=350,y=50)

l1=Label(root,text="USERNAME",bg="black",fg="white",font=("Lucida Handwriting",17))
t1=Entry(root,width="35",textvariable=txtusername)
l1.place(x=800,y=250)
t1.place(x=1000,y=250)

l2=Label(root,text="PASSWORD",bg="black",fg="white",font=("Lucida Handwriting",17))
t2=Entry(root,width="35",textvariable=txtpassword,show="*",fg="black")
l2.place(x=800,y=350)
t2.place(x=1000,y=350)

b1=Button(root,text="Login",width="15",command=login_clicked,fg="white",bg="black",font=("Lucida Handwriting",14))
b2=Button(root,text="Create User",width="15",command=createuser_clicked,fg="white",bg="black",font=("Lucida Handwriting",14))
b3=Button(root,text="Exit",width="15",command=exit_clicked,fg="white",bg="black",font=("Lucida Handwriting",14))
b1.place(x=200,y=700)
b2.place(x=550,y=700)
b3.place(x=900,y=700)

root.mainloop() 
