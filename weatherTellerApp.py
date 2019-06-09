from tkinter import *
from PIL import ImageTk, Image
import os
from weatherTeller import *
import datetime

master = Tk()

master.title("Weather Teller")
master.configure(bg = 'white')

n = 0
t = '00:00:00'

def n0func():
	n = 0
def n1func():
	n = 1
def n2func():
	n = 2
def n3func():
	n = 3
def n4func():
	n = 4

def func00():
	t = '00:00:00'
def func03():
	t = '03:00:00'
def func06():
	t = '06:00:00'
def func09():
	t = '09:00:00'
def func12():
	t = '12:00:00'
def func15():
	t = '15:00:00'
def func18():
	t = '18:00:00'
def func21():
	t = '21:00:00'





img = ImageTk.PhotoImage(Image.open("WeatherLogo.jpeg"))
panel = Label(master, image=img)
panel.pack(side="top", fill="none",expand="no")

locationLabel = Label(master, text="Enter Location: ")
locationLabel.configure(bg = 'white')
locationLabel.place(relx=0.40, rely=0.50, anchor="center")
locationTextbox = Entry(master)
locationTextbox.place(relx=0.55, rely=0.50, anchor="center")
location = locationTextbox.get()

dateLabel = Label(master, text="Choose date: ")
dateLabel.configure(bg = 'white')
dateLabel.place(relx=0.10, rely=0.55, anchor="center")
n0button = Button(master, text=str(datetime.date.today()),command=n0func)
n0button.place(relx=0.25, rely=0.55, anchor="center")
n1button = Button(master, text=str(datetime.date.today()+datetime.timedelta(days=1)),command=n1func)
n1button.place(relx=0.35, rely=0.55, anchor="center")
n2button = Button(master, text=str(datetime.date.today()+datetime.timedelta(days=2)),command=n2func)
n2button.place(relx=0.45, rely=0.55, anchor="center")
n3button = Button(master, text=str(datetime.date.today()+datetime.timedelta(days=3)),command=n3func)
n3button.place(relx=0.55, rely=0.55, anchor="center")
n4button = Button(master, text=str(datetime.date.today()+datetime.timedelta(days=4)),command=n4func)
n4button.place(relx=0.65, rely=0.55, anchor="center")

timeLabel = Label(master, text="Choose time: ")
timeLabel.configure(bg = 'white')
timeLabel.place(relx=0.10, rely=0.60, anchor="center")
button00 = Button(master, text="12 AM",command=func00)
button00.place(relx=0.25, rely=0.60, anchor="center")
button03 = Button(master, text="3 AM",command=func03)
button03.place(relx=0.35, rely=0.60, anchor="center")
button06 = Button(master, text="6 AM",command=func06)
button06.place(relx=0.45, rely=0.60, anchor="center")
button09 = Button(master, text="9 AM",command=func09)
button09.place(relx=0.55, rely=0.60, anchor="center")
button12 = Button(master, text="12 PM",command=func12)
button12.place(relx=0.65, rely=0.60, anchor="center")
button15 = Button(master, text="3 PM",command=func15)
button15.place(relx=0.75, rely=0.60, anchor="center")
button18 = Button(master, text="6 PM",command=func18)
button18.place(relx=0.85, rely=0.60, anchor="center")
button21 = Button(master, text="9 PM",command=func21)
button21.place(relx=0.95, rely=0.60, anchor="center")



mainloop()