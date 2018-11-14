from dashboard2 import *
from connect import *
from controller import *

class Program():

    def __init__(self):

        self.model = Model()
        self.top = Tk()
        self.dashboard = Dashboard(self.top,self.model)
        self.top.mainloop()

main = Program()
    
