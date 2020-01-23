import math

class Drug:
    def __init__(self, name="generic", strengths=[5]):
        self.name=name
        self.strengths=strengths

    def Print(self):
        print("Drug name: <",self.name,">, unit strengths:", self.strengths)

class Temodar(Drug):
    def __init__(self):
        super().__init__("temodar",[250,100,20,5])
    
    def UnitCounts(self,dose):
        dose_covered=0
        count250=(dose-dose_covered) // 250
        dose_covered=dose_covered+250*count250
        count100=(dose-dose_covered) // 100
        dose_covered=dose_covered+100*count100
        count20=(dose-dose_covered) // 20
        dose_covered=dose_covered+20*count20
        count5=(dose-dose_covered) // 5
        dose_covered=dose_covered+5*count5
        return [count250,count100,count20,count5]

    def DoseCovered(self,pCounts):
        return pCounts[0]*250+pCounts[1]*100+pCounts[2]*20+pCounts[3]*5

    def DoseError(self,dose,counts):
        return self.DoseCovered(counts)-dose

    def Dispense(self,patient,first_dose):
        dose=patient.TemodarDose(first_dose)
        return self.UnitCounts(dose)

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
        if firstDose in set(["y","Y"]):
            return 150*self.BSA
        else:
            return 200*self.BSA

def Main():
    print("My name is _______________ and my student number is _____________")
    body_weight=input("Input body weight (kg): ")
    body_height=input("Input body height (cm): ")
    first_dose=input("Is this the first dose (Y/N): ")
    p=Patient("Alice",body_weight,body_height)
    temodar_dose=p.TemodarDose(first_dose)
    p.Print()   
    print("Temodar dose for patient ",p.name,"is",temodar_dose,"mg")
    t=Temodar()
    t.Print()
    pill_count=t.Dispense(p,first_dose)
    print("Temodar Unit Counts:", pill_count[0], " of 250mg, ",pill_count[1], " of 100mg, ", pill_count[2]," of 20mg, ", pill_count[3], " of 5mg" )
    print("Temodar dose covered: ",t.DoseCovered(pill_count),"mg/day")
    print("Temodar dose error: ",t.DoseError(temodar_dose,pill_count),"mg/day")

Main()
