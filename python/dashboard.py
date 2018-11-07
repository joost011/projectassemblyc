from tkinter import *
from tkinter import ttk
import random
import sched, time
from plot import *
import threading


top = Tk()
top.iconbitmap('icon.ico')
top.title('ZENG ltd. - Central Software')

can = Canvas(top, height=750, width=200, highlightthickness=0)
can1 = Canvas(top, height=750, width=800, highlightthickness=0)
can2 = Canvas(top, height=750, width=200, highlightthickness=0)
can.pack_propagate(False)
can1.grid_propagate(False)
can2.pack_propagate(False)

can.create_line(199,0,199,750)

frame1 = Frame(can,width=180,height=120, bd=1, relief='solid')
frame1.pack_propagate(False)
frame1.pack(pady=40)

tempLabel = Label(frame1,text="Temperatuursgrenzen")
tempLabel.pack()

minTempLabel = Label(frame1,text="Minimumgrens:")
minTempLabel.pack()
minTemp = Entry(frame1)
minTemp.pack()

maxTempLabel = Label(frame1,text="Maximumgrens:")
maxTempLabel.pack()
maxTemp = Entry(frame1)
maxTemp.pack()

frame2 = Frame(can,width=180,height=120, bd=1, relief='solid')
frame2.pack_propagate(False)
frame2.pack(pady=40)

lightLabel = Label(frame2,text="Lichtgrenzen")
lightLabel.pack()

minLightLabel = Label(frame2,text="Minimumgrens:")
minLightLabel.pack()
minLight = Entry(frame2)
minLight.pack()

maxLightLabel = Label(frame2,text="Maximumgrens:")
maxLightLabel.pack()
maxLight = Entry(frame2)
maxLight.pack()

frame3 = Frame(can,width=180,height=120, bd=1, relief='solid')
frame3.pack_propagate(False)
frame3.pack(pady=40)

lengthLabel = Label(frame3,text="Lengte")
lengthLabel.pack()

minLengthLabel = Label(frame3,text="Minimale uitrollengte:")
minLengthLabel.pack()
minLength = Entry(frame3)
minLength.pack()

maxLengthLabel = Label(frame3,text="Maximale uitrollengte:")
maxLengthLabel.pack()
maxLength = Entry(frame3)
maxLength.pack()

B = ttk.Button(can, text ="Update settings")	
B.pack()

can2.create_line(0,0,0,750)

frame4 = Frame(can2,width=180,height=170, bd=1, relief='solid')
frame4.pack_propagate(False)
frame4.pack(pady=40)

current = Label(frame4,text="Huidige waarden", font="'Arial', 15", pady=10)
current.pack()
currentTemp = Label(frame4,text="Huidige temperatuur: 20")
currentTemp.pack()
currentLight = Label(frame4,text="Huidige lichtsterkte: 1350")
currentLight.pack()
currentStatus = Label(frame4,text="Zonnescherm: ingerold",pady=10)
currentStatus.pack()

frame5 = Frame(can2,width=180,height=170, bd=1, relief='solid')
frame5.pack_propagate(False)
frame5.pack(pady=20)

manual = Label(frame5,text="Handmatige bediening", font="'Arial', 13", pady=10)
manual.pack()
rollOutButton = ttk.Button(frame5, text ="Uitrollen")
rollOutButton.pack()
rollInButton = ttk.Button(frame5, text ="Inrollen")
rollInButton.pack(pady=10)

can.pack(side="left")
can1.pack(side="left")
can2.pack(side="left")

logo = PhotoImage(file='logo.png')
logolabel = Label(can1, image = logo)
logolabel.grid(row=1,column=2)
plot1 = Plot(can1, 1,1, 'temp')
plot2 = Plot(can1, 2,1, 'light')
plot3 = Plot(can1, 2,2, '')
plot4 = Plot(can1, 3,1, '')
plot5 = Plot(can1, 3,2, '')


top.mainloop()
