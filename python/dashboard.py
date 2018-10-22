import tkinter
import random
import sched, time

top = tkinter.Tk()

can = tkinter.Canvas(top, height=600, width=200, highlightthickness=0)
can1 = tkinter.Canvas(top, height=600, width=800, highlightthickness=0)
can.pack_propagate(False)
can1.pack_propagate(False)

can.create_line(199,0,199,600)

frame1 = tkinter.Frame(can,width=180,height=120, bd=1, relief='solid')
frame1.pack_propagate(False)
frame1.pack(pady=30)

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
frame2.pack(pady=30)

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
frame3.pack(pady=30)

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

can.pack(side="left")
can1.pack(side="left")
top.mainloop()