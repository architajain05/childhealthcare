from tkinter import*
def b1():
    import Application.py
def b2():
    import Application.py
def b3():
    import Blood.py
def b4():
    import Application.py
def b5():
    import Application.py
def b6():
    import Application.py

root = Tk()
root.geometry("1000x1000")
root.configure(bg="cyan")
root.title("Menu screen")
root.state("zoomed")


test=Label(text="Menu Screen",font='algerian 48',bg='yellow',fg='dark blue',borderwidth=6 )
test.place(x=550,y=0)

b1=Button(text="Book An Appointment",font="100",command=b1,borderwidth=10,width=30)
b1.place(x=600,y=350)

b2=Button(text="Vaccine",font="24",command=b2,borderwidth=10, width=30)
b2.place(x=600,y=250)

b3=Button(text="Payement",font="24",command=b3,borderwidth=10, width=30)
b3.place(x=600,y=450)



b5=Button(text="FAQ",font="24",command=b5,borderwidth=10, width=30)
b5.place(x=600,y=550)




root.mainloop()