import math

class Patient:
    def __init__(self, n="anonymous", w=0, h=0):
        self.name=n
        self.weight=w
        self.height=h
    
    @property
    def BSA(self):
        return math.exp(
         0.425*math.log(float(self.weight))
        +0.725*math.log(float(self.height))
        +math.log(71.84))/10000
    
    def Print(self):
        print("Patient name: <",self.name,">, weight=",self.weight,"kg, height=",self.height,"cm")

    def TemodarDose(self,firstDose):
        


def Main():
    print("My name is _______________ and my student number is _____________")

    body_weight=input("Input body weight (kg): ")
    body_height=input("Input body height (cm): ")
    first_dose=input("Is this the first dose (Y/N): ")

    p=Patient("Alice",body_weight,body_height)
    p.Print()
    print(".")
    
 
Main()
