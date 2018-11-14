from tkinter import *
from tkinter import ttk
import random
from connect import *
from plot import *
from controller import *

class Dashboard():

    def __init__(self,master,model):
        self.master = master
        self.model = model
        self.createWidgets()
        self.controller = Controller(self.model,self)
        self.master.iconbitmap('icon.ico')
        self.master.title('ZENG ltd. - Central Software')


    def createWidgets(self):
        self.can = Canvas(self.master, height=750, width=200, highlightthickness=0)
        self.can1 = Canvas(self.master, height=750, width=800, highlightthickness=0)
        self.can2 = Canvas(self.master, height=750, width=200, highlightthickness=0)
        self.can.pack_propagate(False)
        self.can1.grid_propagate(False)
        self.can2.pack_propagate(False)

        self.can.create_line(199,0,199,750)

        self.frame1 = Frame(self.can,width=180,height=120,bd=1,relief='solid')
        self.frame1.pack(pady=40)
        self.frame1.pack_propagate(False)
        self.tempLabel = Label(self.frame1,text='Temperatuursgrenzen')
        self.tempLabel.pack()
        self.minTempLabel = Label(self.frame1,text='Minimumgrens:')
        self.minTempLabel.pack()
        self.minTemp = Entry(self.frame1)
        self.minTemp.pack()
        self.maxTempLabel = Label(self.frame1,text='Maximumgrens:')
        self.maxTempLabel.pack()
        self.maxTemp = Entry(self.frame1)
        self.maxTemp.pack()

        self.frame2 = Frame(self.can,width=180,height=120,bd=1,relief='solid')
        self.frame2.pack(pady=40)
        self.frame2.pack_propagate(False)
        self.lightLabel = Label(self.frame2,text='Lightgrenzen')
        self.lightLabel.pack()
        self.minLightLabel = Label(self.frame2,text='Minimumgrens:')
        self.minLightLabel.pack()
        self.minLight = Entry(self.frame2)
        self.minLight.pack()
        self.maxLightLabel = Label(self.frame2,text='Maximumgrens')
        self.maxLightLabel.pack()
        self.maxLight = Entry(self.frame2)
        self.maxLight.pack()

        self.frame3 = Frame(self.can,width=180,height=120,bd=1,relief='solid')
        self.frame3.pack(pady=40)
        self.frame3.pack_propagate(False)
        self.lenghtLabel = Label(self.frame3,text='Lengte')
        self.lenghtLabel.pack()
        self.minLengthLabel = Label(self.frame3,text='Minimale uitrollengte:')
        self.minLengthLabel.pack()
        self.minLength = Entry(self.frame3)
        self.minLength.pack()
        self.maxLengthLabel = Label(self.frame3,text="Maximale uitrollengte:")
        self.maxLengthLabel.pack()
        self.maxLength = Entry(self.frame3)
        self.maxLength.pack()

        self.B = ttk.Button(self.can, text ="Update settings", command=self.updateGrenzen)	
        self.B.pack()

        self.can2.create_line(0,0,0,750)

        self.frame4 = Frame(self.can2,width=180,height=170, bd=1, relief='solid')
        self.frame4.pack_propagate(False)
        self.frame4.pack(pady=40)
        self.current = Label(self.frame4,text="Huidige waarden", font="'Arial', 15", pady=10)
        self.current.pack()
        self.currentTemp = Label(self.frame4,text="Huidige temperatuur: 0")
        self.currentTemp.pack()
        self.currentLight = Label(self.frame4,text="Huidige lichtsterkte: 1350")
        self.currentLight.pack()
        self.currentStatus = Label(self.frame4,text="Zonnescherm: ingerold",pady=10)
        self.currentStatus.pack()

        self.frame5 = Frame(self.can2,width=180,height=170, bd=1, relief='solid')
        self.frame5.pack_propagate(False)
        self.frame5.pack(pady=20)

        self.manual = Label(self.frame5,text="Handmatige bediening", font="'Arial', 13", pady=10)
        self.manual.pack()
        self.rollOutButton = ttk.Button(self.frame5, text ="Uitrollen")
        self.rollOutButton.pack()
        self.rollInButton = ttk.Button(self.frame5, text ="Inrollen")
        self.rollInButton.pack(pady=10)

        self.can.pack(side="left")
        self.can1.pack(side="left")
        self.can2.pack(side="left")

        self.logo = PhotoImage(file='logo.png')
        self.logolabel = Label(self.can1, image = self.logo)
        self.logolabel.grid(row=1,column=1)
        self.plot1 = Plot(self.can1, 2,1, 'temp',self.model)
        self.plot2 = Plot(self.can1, 3,1, 'light',self.model)


    def updateStats(self):
        self.currentTemp['text'] = 'Huidige temperatuur: ' + str(self.model.sensor1[8])
        self.currentLight['text'] = 'Huidige lichtstertke: ' + str(self.model.sensor2[8])
        self.plot1.redraw()
        self.plot2.redraw()
        self.master.after(100, self.updateStats)

    def updateGrenzen(self):
        mintemp = self.minTemp.get()
        maxtemp = self.maxTemp.get()
        minlight = self.minLight.get() 
        maxlight = self.maxLight.get() 
        minlength = self.minLength.get() 
        maxlength = self.maxLength.get()
        self.model.sender(mintemp,maxtemp,minlight,maxlight,minlength,maxlength)
         
        
    
