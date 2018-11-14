from connect import *
import threading

class Controller():

    def __init__(self,model,dashboard):
        self.model = dashboard.model
        self.dashboard = dashboard
        self.getStats()
        

    def getStats(self):
        t1 = threading.Thread(target=self.model.receiver)
        t1.start()
        self.dashboard.updateStats()
        
        

    
        
