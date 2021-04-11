import time
print("Choose any two chemicals from below to be combined: ")
print("Oxygen, Carbon, Hydrogen, Chlorine")
time.sleep(0)
chem1= input("Enter your first choice: ")
chem2= input("Enter your second choice: ")
print("")

if chem1=="Oxygen" or chem1=="oxygen":
    if chem2=="Carbon" or chem2=="carbon":
        print("Result: Carbon dioxide or Carbon Monoxide")
    elif chem2=="Hydrogen" or chem2=="hydrogen":
        print("Result: Water")
    elif chem2=="Chlorine" or chem2=="chlorine":
        print("Result: Dichlorine Heptoxide")
        
elif chem1=="Carbon" or chem1=="carbon":
    if chem2=="Oxygen" or chem2=="oxygen":
        print("Result: Carbon dioxide or Carbon Monoxide")
    elif chem2=="Hydrogen" or chem2=="hydrogen":
        print("Result: Methane")
    elif chem2=="Chlorine" or chem2=="chlorine":
        print("Result: Tetrachloromethane")
        
elif chem1=="Hydrogen" or chem1=="hydrogen":
    if chem2=="Oxygen" or chem2=="oxygen":
        print("Result: Water")
    elif chem2=="Carbon" or chem2=="carbon":
        print("Result: Methane")
    elif chem2=="Chlorine" or chem2=="chlorine":
        print("Result: Hydrogen Chloride")
        
elif chem1=="Chlorine" or chem1=="chlorine":
    if chem2=="Oxygen" or chem2=="oxygen":
        print("Result: Dichlorine Heptoxide")
    elif chem2=="Hydrogen" or chem2=="hydrogen":
        print("Result: Hydrogen Chloride")
    elif chem2=="Carbon" or chem2=="carbon":
        print("Result: Tetrachloromethane")
        
else:
    print("Chemical names not valid")
    
print("Thank You!")