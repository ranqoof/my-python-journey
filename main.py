#I have not used math module as it would be little easy so i have only used arthmetic operators of python 3.14 time module for making it a bit realism



import time

print("-------------------Many Calc-------------------")
print("1.Area\n2.Perimeter")
words=["area","perimeter"]
while True:
    type=str(input("Type the type of calculation: "))
    type = type.lower()
    if type in words:
           break
    else:
           print("Try typing again you fat fingersa")
    
if type=="area":
    print("Which shape: \n1. Rectangle \n2. Circle\n3. Triangle \n4. Square\n5. Cyclinder")
    type=str(input("Type the type of Shape: "))
    type=type.lower()
    if type=="rectangle":
            L = float(input("Length: "))
            B = float(input("Breadth: "))
            print("Loading..")
            time.sleep(1)
            print("The Area of the Rectangle in cm is",round(L*B,2),"sqcm")
    elif type=="circle":
            L = float(input("Radius: "))
            print("Loading..")
            time.sleep(1)
            print("The Area of the Circle in cm is",round(22/7*L**2,2),"sqcm")
    elif type=="triangle":
            L = float(input("Height: "))
            B = float(input("Base: "))
            print("Loading..")
            time.sleep(1)
            print("The Area of the Triangle in cm is",round(1/2*L*B,2),"sqcm")
    elif type=="square":
            L = float(input("Length: "))
            print("Loading..")
            time.sleep(1)
            print("The Area of the Square in cm is",round(L**2,2),"sqcm")
    elif type=="cyclinder":
            L = float(input("Height: "))
            B = float(input("Radius: "))
            print("Loading..")
            time.sleep(1)
            print("The Total surface Area of the Cyclinder in cm is",round(2*22/7*B*L,2),"sqcm")
elif type=="perimeter":
    print("Which shape: \n1. Rectangle \n2. Circle\n3. Equilateral Triangle \n4. Square\n5. Cyclinder")
    type=str(input("Type the type of Shape: "))
    type=type.lower()
    if type=="rectangle":
            L = float(input("Length: "))
            B = float(input("Breadth: "))
            print("Loading..")
            time.sleep(1)
            print("The Perimeter of the Rectangle in cm is",2*L+2*B,"cm")
    elif type=="circle":
            L = float(input("Radius: "))
            print("Loading..")
            time.sleep(1)
            print("The Perimeter of the Circle in cm is",2*22/7*L,"sqcm")
    elif type=="triangle":
            L = float(input("Length of one side: "))
            
            print("Loading..")
            time.sleep(1)
            print("The Perimeter of the Triangle in cm is",3*L,"sqcm")
    elif type=="square":
            L = float(input("Length: "))
            print("Loading..")
            time.sleep(1)
            print("The Perimeter of the Square in cm is",L**2,"sqcm")
    elif type=="cyclinder":
            L = float(input("Height: "))
            B = float(input("Radius: "))
            print("Loading..")
            time.sleep(1)
            print("The Perimeter of the Cyclinder in cm is",(2*(2*B)+2*L),"cm")

           
time.sleep(2)

print("I hope you like it")


time.sleep(1)
print(input("Press Enter to Exit...."))
    
    