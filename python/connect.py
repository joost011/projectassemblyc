import serial
import binascii
from controller import *

ser = serial.Serial("COM5", 19200)

class Model():

    def __init__(self):
        self.sensor1 = [0,0,0,0,0,0,0,0,0]
        self.sensor2 = [0,0,0,0,0,0,0,0,0]
        self.sensor1time = [0,0,0,0,0,0,0,0,0]
        self.sensor2time = [0,0,0,0,0,0,0,0,0]
        self.inittime1 = 0
        self.inittime2 = 0
        self.mode = 0
    
    def receiver(self):
        while 1:
            value = ser.read()
            value = binascii.hexlify(value)
            if self.mode == 0:
                print('Sensor1: ',int(value,16))
                del self.sensor1[0]
                self.sensor1.append(int(value,16))
                self.inittime1 += 10
                del self.sensor1time[0]
                self.sensor1time.append(self.inittime1)
                self.mode = 1
            else:
                print('Sensor2: ',int(value,16))
                del self.sensor2[0]
                self.sensor2.append(int(value,16))
                self.inittime2 += 10
                del self.sensor2time[0]
                self.sensor2time.append(self.inittime2)
                self.mode = 0

    def sender(self,mintemp,maxtemp,minlight,maxlight,minlength,maxlength):
        self.mintemp = mintemp
        self.maxtemp = maxtemp
        self.minlight = minlight
        self.maxlight = maxlight
        self.minlength = minlength
        self.maxlength = maxlength
        mintemp = int(mintemp)
        mintemp = hex(mintemp)
        mintemp = bytes(mintemp, encoding='utf-8')
        maxtemp = int(maxtemp)
        maxtemp = hex(mintemp)
        maxtemp = bytes(maxtemp, encodig='utf-8')
        minlight = int(minlight)
        minlight = hex(minlight)
        minlight = bytes(minlight, encodig='utf-8')
        print(mintemp)
        print(maxtemp)
        ser.write(mintemp)
        ser.write(maxtemp)
        ser.write(minlight)
        #ser.write(minlight.encode())
        #ser.write(maxlight.encode())
        
    
