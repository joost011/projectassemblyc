import serial
import tkinter
import sched, time
import threading
import struct

ser = serial.Serial("COM3", 19200)

def receiver():
    global sensor1
    global sensor2
    number = 0
    gem = 0
    mode = 0
    sensor1 = [0,0,0,0,0,0,0,0,0]
    sensor2 = [0,0,0,0,0,0,0,0,0]
    while 1:
            value = str(ser.read())
            if mode == 0:
                    if "x" in value:
                            print(value)
                            value = value[4:6]
                            print("Temperatuur:",value)
                            del sensor1[0]
                            sensor1.append(int(value,16))
                            print(sensor1)
                    mode = 0
            else:
                if 'x' in value:
                    value = value[4:6]
                    print("Licht:",int(value,16))
                    del sensor2[0]
                    sensor2.append(int(value,16))
                mode = 0

t = threading.Thread(target=receiver)
t.start()
