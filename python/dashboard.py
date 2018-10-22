import tkinter
import random
import sched, time

top = tkinter.Tk()

can = tkinter.Canvas(top, height=750, width=200, highlightthickness=0)
can1 = tkinter.Canvas(top, height=750, width=800, highlightthickness=0)
can2 = tkinter.Canvas(top, height=750, width=200, highlightthickness=0)
can.pack_propagate(False)
can1.pack_propagate(False)
can2.pack_propagate(False)

can.create_line(199,0,199,750)

frame1 = tkinter.Frame(can,width=180,height=120, bd=1, relief='solid')
frame1.pack_propagate(False)
frame1.pack(pady=40)

tempLabel = tkinter.Label(frame1,text="Temperatuursgrenzen:")
tempLabel.pack()

minTempLabel = tkinter.Label(frame1,text="Minimumgrens:")
minTempLabel.pack()
minTemp = tkinter.Entry(frame1)
minTemp.pack()

maxTempLabel = tkinter.Label(frame1,text="Maximumgrens:")
maxTempLabel.pack()
maxTemp = tkinter.Entry(frame1)
maxTemp.pack()

frame2 = tkinter.Frame(can,width=180,height=120, bd=1, relief='solid')
frame2.pack_propagate(False)
frame2.pack(pady=40)

lightLabel = tkinter.Label(frame2,text="Lichtgrenzen:")
lightLabel.pack()

minLightLabel = tkinter.Label(frame2,text="Minimumgrens:")
minLightLabel.pack()
minLight = tkinter.Entry(frame2)
minLight.pack()

maxLightLabel = tkinter.Label(frame2,text="Maximumgrens:")
maxLightLabel.pack()
maxLight = tkinter.Entry(frame2)
maxLight.pack()

frame3 = tkinter.Frame(can,width=180,height=120, bd=1, relief='solid')
frame3.pack_propagate(False)
frame3.pack(pady=40)

lengthLabel = tkinter.Label(frame3,text="Lengte:")
lengthLabel.pack()

minLengthLabel = tkinter.Label(frame3,text="Minimale uitrollengte:")
minLengthLabel.pack()
minLength = tkinter.Entry(frame3)
minLength.pack()

maxLengthLabel = tkinter.Label(frame3,text="Maximale uitrollengte:")
maxLengthLabel.pack()
maxLength = tkinter.Entry(frame3)
maxLength.pack()

B = tkinter.Button(can, text ="Update settings")	
B.pack()

can2.create_line(0,0,0,750)

frame4 = tkinter.Frame(can2,width=180,height=170, bd=1, relief='solid')
frame4.pack_propagate(False)
frame4.pack(pady=40)

current = tkinter.Label(frame4,text="Huidige waarden", font="'Arial', 15", pady=10)
current.pack()
currentTemp = tkinter.Label(frame4,text="Huidige temperatuur: 20")
currentTemp.pack()
currentLight = tkinter.Label(frame4,text="Huidige lichtsterkte: 1350")
currentLight.pack()
currentStatus = tkinter.Label(frame4,text="Zonnescherm: ingerold",pady=10)
currentStatus.pack()

frame5 = tkinter.Frame(can2,width=180,height=170, bd=1, relief='solid')
frame5.pack_propagate(False)
frame5.pack(pady=20)

manual = tkinter.Label(frame5,text="Handmatige bediening", font="'Arial', 13", pady=10)
manual.pack()
rollOutButton = tkinter.Button(frame5, text ="Uitrollen")
rollOutButton.pack()
rollInButton = tkinter.Button(frame5, text ="Inrollen")
rollInButton.pack(pady=10)

can.pack(side="left")
can1.pack(side="left")
can2.pack(side="left")
top.mainloop()