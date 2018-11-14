import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from tkinter import ttk
import random
from connect import *

rows = {2:110, 3:380}

class Plot():


    def __init__(self, master, row, col, typ, model):

        self.model = model
        self.master = master
        self.typ = typ
        if typ == 'temp':
            self.values = model.sensor1
            self.currentTemp = model.sensor1[8]
            self.time = model.sensor1time
        if typ == 'light':
            self.values = model.sensor2
            self.currentLight = model.sensor2[8]
            self.time = model.sensor2time
        self.f = Figure(figsize=(5.2,2.3))
        self.f.patch.set_facecolor('#F0F0F0')
        self.a = self.f.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.f, master)
        self.canvas.get_tk_widget().grid(row = row, column = col, padx=100, pady = 20, sticky=E)
        self.f.tight_layout(pad = 0.1)

        if self.typ is not '':
            self.dot = PhotoImage(file='cam.png')
            self.dotlabel = Label(master, image = self.dot, cursor = 'hand2')
            self.dotlabel.place(x=590,y=rows[row])
            self.dotlabel.bind('<Button-1>',self.screenshot)
     
    def redraw(self):
        self.a.clear()
        if self.typ == 'temp':
            self.a.set_title('Temperatuursensor')
            self.a.set_ylabel('Temp. in °C')
            self.a.set_xlabel('Tijd in seconden')
            self.a.set_ylim(([(min(self.values)-1),(max(self.values)+1)]))
        if self.typ == 'light':
            self.a.set_title('Lichtsensor')
            self.a.set_ylabel('Lichtst. in lux')
            self.a.set_xlabel('Tijd in seconden')
            self.a.set_ylim(([(min(self.values)-1),(max(self.values)+1)]))
        self.f.tight_layout(pad = 0.1)
        self.a.plot(self.time,self.values)
        self.canvas.draw()

    def screenshot(self,event):
        sswindow = ScreenshotWindow(self.f,self.typ,self.values)



class ScreenshotWindow():
    

    def __init__(self,fig,typ,val):
        self.window = Tk()
        self.window.resizable(False,False)
        self.window.iconbitmap('icon.ico')
        self.window.title('ZENG ltd. - Save Screenshot')
        self.val = val
        self.typ = typ
        self.fig = Figure(figsize=(5.2,2.3))
        self.fig.patch.set_facecolor('#F0F0F0')
        self.fig.tight_layout(pad=0.1)
        self.sp = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig,self.window)
        self.canvas.get_tk_widget().grid(row=1,column=1,columnspan=2,padx=20,pady=20)
        if self.typ == 'temp':
            self.sp.set_title('Temperatuursensor')
            self.sp.set_ylabel('Temp. in °C')
            self.sp.set_xlabel('Tijd in seconden')
            self.fig.tight_layout(pad=0.1)
        if self.typ == 'light':
            self.sp.set_title('Lichtsensor')
            self.sp.set_ylabel('Lichtst. in lux')
            self.sp.set_xlabel('Tijd in seconden')
            self.fig.tight_layout(pad=0.1)
        self.sp.plot([1,2,3,4,5,6,7,8,9],self.val)
        self.canvas.draw()
        self.entry = Entry(self.window, width=50)
        self.entry.grid(row=2,column=1)
        self.savebutton = ttk.Button(self.window,text='Save',command=self.save)
        self.savebutton.grid(row=2,column=2)
        self.meslabel = Label(self.window,text='')
        self.meslabel.grid(row=3,column=1,columnspan=2,pady=10)

    def save(self):
        forbchar = ['"', '*', ':', '?', '/', '\ ', '|', '<', '>']
        error = 0
        if self.entry.get() == '':
            self.meslabel['fg'] = 'red'
            self.meslabel['text'] = 'Voer alstublieft de gewenste bestandsnaam in!'
            error = 1
        for x in self.entry.get():
            if x in forbchar:
               self.meslabel['fg'] = 'red'
               self.meslabel['text'] = 'De volgende karakters zijn niet toegestaan in de bestandsnaam: " * : ? / \ | < >'
               error = 1
        if error == 0:
            self.meslabel['fg'] = 'green'
            self.meslabel['text'] = 'De afbeelding is opgeslagen!'
            self.fig.savefig('screenshots/' + self.entry.get() + '.png')
