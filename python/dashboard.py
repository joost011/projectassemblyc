import tkinter
import random
import sched, time

top = tkinter.Tk()

can = tkinter.Canvas(top, height=700, width=200)
can.pack(side="left")
can1 = tkinter.Canvas(top, height=700, width=800)
can1.pack(side="left")

tempLabel = tkinter.Label(can,text="Temperatuursgrenzen:")
tempLabel.pack()

minTempLabel = tkinter.Label(can,text="Minimumgrens:")
minTempLabel.pack()
minTemp = tkinter.Entry(can)
minTemp.pack()

maxTempLabel = tkinter.Label(can,text="Maximumgrens:")
maxTempLabel.pack()
maxTemp = tkinter.Entry(can)
maxTemp.pack()

line = canvas.create_line(x0, y0, x1, y1, ..., xn, yn, options)

top.mainloop()