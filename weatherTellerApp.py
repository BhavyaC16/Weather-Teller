# AUTHOR: BHAVYA CHOPRA 

from tkinter import *
from PIL import ImageTk, Image
from os import *
from weatherTeller import *
import datetime

master = Tk()

master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))

master.title("Weather Teller")
master.configure(bg = 'white')

n = 0
t = '00:00:00'

def submitfunc():
	location = locationTextbox.get()
	json = weather_response(location)
	if(n0var.get()==1):
		n = 0
	elif(n1var.get()==1):
		n = 1
	elif(n2var.get()==1):
		n = 2
	elif(n3var.get()==1):
		n = 3
	elif(n4var.get()==1):
		n = 4
	if(var00.get()==1):
		t = '00:00:00'
	elif(var03.get()==1):
		t = '03:00:00'
	elif(var06.get()==1):
		t = '06:00:00'
	elif(var09.get()==1):
		t = '09:00:00'
	elif(var12.get()==1):
		t = '12:00:00'
	elif(var15.get()==1):
		t = '15:00:00'
	elif(var18.get()==1):
		t = '18:00:00'
	elif(var21.get()==1):
		t = '21:00:00'
	
	temp = int(get_temperature(json,n,t)) - 273
	humidity = get_humidity(json,n,t)
	pressure = float(get_pressure(json,n,t))*100
	wind = get_wind(json,n,t)
	sealevel = get_sealevel(json,n,t)
	tempLabel = Label(master, text=("Temperature:  "+str(temp)+" °C"))
	tempLabel.configure(bg = 'white')
	tempLabel.place(relx = 0.40, rely = 0.70, anchor="center")
	humidityLabel = Label(master, text=("Humidity:  "+str(humidity)+"%"))
	humidityLabel.configure(bg = 'white')
	humidityLabel.place(relx = 0.60, rely = 0.70, anchor="center")
	pressureLabel = Label(master, text=("Pressure:  "+str(pressure)+" Pa"))
	pressureLabel.configure(bg = 'white')
	pressureLabel.place(relx = 0.40, rely = 0.75, anchor="center")
	windLabel = Label(master, text=("Wind Speed:  "+str(wind)+" kmph"))
	windLabel.configure(bg = 'white')
	windLabel.place(relx = 0.60, rely = 0.75, anchor="center")
	seaLabel = Label(master, text=("Sea Level:  "+str(sealevel)+" mm"))
	seaLabel.configure(bg = 'white')
	seaLabel.place(relx = 0.50, rely = 0.80, anchor="center")

img = ImageTk.PhotoImage(Image.open("WeatherLogo.jpeg"))
panel = Label(master, image=img)
panel.pack(side="top", fill="none",expand="no")

titleLabel1 = Label(master, text="Weather")
titleLabel1.config(font=("Arial",50), bg = 'white')
titleLabel1.place(relx = 0.26, rely = 0.15, anchor = "center")
titleLabel2 = Label(master, text="Teller")
titleLabel2.config(font=("Arial",50), bg = 'white')
titleLabel2.place(relx = 0.70, rely = 0.15, anchor = "center")


locationLabel = Label(master, text="Enter Location: ")
locationLabel.configure(bg = 'white')
locationLabel.place(relx=0.40, rely=0.30, anchor="center")
locationTextbox = Entry(master)
locationTextbox.place(relx=0.55, rely=0.30, anchor="center")


dateLabel = Label(master, text="Choose date: ")
dateLabel.configure(bg = 'white')
dateLabel.place(relx=0.35, rely=0.35, anchor="center")
n0var = IntVar()
n1var = IntVar()
n2var = IntVar()
n3var = IntVar()
n4var = IntVar()
n0check = Checkbutton(master, text=str(datetime.date.today()), variable=n0var, bg='white')
n0check.place(relx=0.45, rely=0.35, anchor="center")
n1check = Checkbutton(master, text=str(datetime.date.today()+datetime.timedelta(days=1)), variable=n1var, bg='white')
n1check.place(relx=0.45, rely=0.38, anchor="center")
n2check = Checkbutton(master, text=str(datetime.date.today()+datetime.timedelta(days=2)), variable=n2var, bg='white')
n2check.place(relx=0.45, rely=0.41, anchor="center")
n3check = Checkbutton(master, text=str(datetime.date.today()+datetime.timedelta(days=3)), variable=n3var, bg='white')
n3check.place(relx=0.45, rely=0.44, anchor="center")
n4check = Checkbutton(master, text=str(datetime.date.today()+datetime.timedelta(days=4)), variable=n4var, bg='white')
n4check.place(relx=0.45, rely=0.47, anchor="center")

timeLabel = Label(master, text="Choose time: ")
timeLabel.configure(bg = 'white')
timeLabel.place(relx=0.60, rely=0.35, anchor="center")
var00 = IntVar()
var03 = IntVar()
var06 = IntVar()
var09 = IntVar()
var12 = IntVar()
var15 = IntVar()
var18 = IntVar()
var21 = IntVar()
check00 = Checkbutton(master, text="12 AM", variable=var00, bg='white')
check00.place(relx=0.70, rely=0.35, anchor="center")
check03 = Checkbutton(master, text="03 AM", variable=var03, bg='white')
check03.place(relx=0.70, rely=0.38, anchor="center")
check06 = Checkbutton(master, text="06 AM", variable=var06, bg='white')
check06.place(relx=0.70, rely=0.41, anchor="center")
check09 = Checkbutton(master, text="09 AM", variable=var09, bg='white')
check09.place(relx=0.70, rely=0.44, anchor="center")
check12 = Checkbutton(master, text="12 PM", variable=var12, bg='white')
check12.place(relx=0.70, rely=0.47, anchor="center")
check15 = Checkbutton(master, text="03 PM", variable=var15, bg='white')
check15.place(relx=0.70, rely=0.50, anchor="center")
check18 = Checkbutton(master, text="06 PM", variable=var18, bg='white')
check18.place(relx=0.70, rely=0.53, anchor="center")
check21 = Checkbutton(master, text="09 PM", variable=var21, bg='white')
check21.place(relx=0.70, rely=0.56, anchor="center")



submission = Button(master, text="Tell Me The Weather!", command=submitfunc)
submission.place(relx = 0.50, rely = 0.61, anchor="center")

mainloop()
