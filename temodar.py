import math

def BSA(bWeight, bHeight):
    return math.exp(
         0.425*math.log(float(bWeight)
        +0.725*math.log(float(bHeight)))
        +math.log(71.84))/10000

def DailyDose(bWeight, bHeight, fDose):
    BSA_value=BSA(bWeight,bHeight)
    if (fDose in set(["y","Y"])):
        return 150*BSA_value
    else:
        return 200*BSA_value

def Main():
    body_weight=input("Input body weight (kg): ")
    body_height=input("Input body height (cm): ")
    first_dose=input("Is this the first dose (Y/N): ")

    print("")
    print("weight=", body_weight, "kg; height=", body_height, "cm\n\n")
    print("BSA=",BSA(body_weight,body_height))
    print("Daily Dose=",DailyDose(body_weight, body_height,first_dose))

Main()
