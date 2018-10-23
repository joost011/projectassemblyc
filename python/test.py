#Afstand sensor: https://howtomechatronics.com/tutorials/arduino/ultrasonic-sensor-hc-sr04/
#Licht sensor: https://maker.pro/arduino/tutorial/how-to-use-an-ldr-sensor-with-arduino
#Temperatuur sensor: https://learn.adafruit.com/tmp36-temperature-sensor/using-a-temp-sensor
#Juiste formule voor Temperatuursensor: https://www.bc-robotics.com/tutorials/using-a-tmp36-temperature-sensor-with-arduino/

import serial
import tkinter
import sched, time

cc = ""
stopy = 0

top = tkinter.Tk()

dist = tkinter.Label(top, text="Distance: ")
dist.pack()
light = tkinter.Label(top, text="Light: ")
light.pack()
temp = tkinter.Label(top, text="Temperature: ")
temp.pack()

ser = serial.Serial("COM3", 9600)

def updateValues():
	global cc
	global stopy
	if stopy == 0:
		return
	cc=str(ser.readline())
	sp = cc[2:][:-5].split(",")
	dist['text'] = "Distance: " + sp[0]
	light['text'] = "Light: " + sp[1]
	temp['text'] = "Temperature: " + sp[2]
	top.after(1000, updateValues)

def start(event):
	global stopy
	if stopy == 0:
		stopy = 1
		updateValues()
		return
	if stopy == 1:
		stopy = 0

top.bind('<Button-1>', start)

top.mainloop()