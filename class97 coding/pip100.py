class Car (object):
    def __init__(self,model,colour,company,speedlimit):
        self.colour=colour
        self.model=model
        self.company=company
        self.speedlimit=speedlimit
        
    def start (self):
        print('started')   
    def stop (self):
        print ('stop')


audi=Car('Q5','white','audi','140')
print(audi.colour) 
print(audi.start())      

class Bike (object):
    def __init__(self,colour,model,company,speedlimit) :
        self.colour=colour
        self.model=model
        self.company=company
        self.speedlimit=speedlimit
    def start (self):
        print('start') 
    def stop (self):
        print ('stop')

activa = Bike('black','activa','honda','80')     
print(activa.colour) 
print(activa.start())    
                