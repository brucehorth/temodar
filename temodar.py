import math

def BSA(bWeight, bHeight):
    return math.exp(
         0.425*math.log(float(bWeight))
        +0.725*math.log(float(bHeight))
        +math.log(71.84))/10000

def DailyDose(bWeight, bHeight, fDose):
    BSA_value=BSA(bWeight,bHeight)
    if (fDose in set(["y","Y"])):
        return 150*BSA_value
    else:
        return 200*BSA_value

def CalcPillCount(bWeight,bHeight,fDose):
    daily_dose=DailyDose(bWeight,bHeight,fDose)
    dose_covered=0
    count250=(daily_dose-dose_covered) // 250
    dose_covered=dose_covered+250*count250
    count100=(daily_dose-dose_covered) // 100
    dose_covered=dose_covered+100*count100
    count20=(daily_dose-dose_covered) // 20
    dose_covered=dose_covered+20*count20
    count5=(daily_dose-dose_covered) // 5
    dose_covered=dose_covered+5*count5
    return [count250,count100,count20,count5]

def DoseCovered(pCounts):
    return pCounts[0]*250+pCounts[1]*100+pCounts[2]*20+pCounts[3]*5

def Main():
    print("My name is _______________ and my student number is _____________")

    body_weight=input("Input body weight (kg): ")
    body_height=input("Input body height (cm): ")
    first_dose=input("Is this the first dose (Y/N): ")
    pill_count=CalcPillCount(body_weight,body_height,first_dose)
    daily_dose=DailyDose(body_weight, body_height,first_dose)
    dose_covered=DoseCovered(pill_count)

    print("")
    print("weight=", body_weight, "kg; height=", body_height, "cm\n\n")
    print("BSA=",BSA(body_weight,body_height)," sq. m")
    print("Daily Dose=",daily_dose,"mg/day")
    print("Dose Covered:", dose_covered, " mg/day")
    print("Pill counts:", pill_count[0], " of 250mg, ",pill_count[1], " of 100mg, ", pill_count[2]," of 20mg, ", pill_count[3], " of 5mg" )
    print("error: ", dose_covered-daily_dose," mg/day")
Main()
