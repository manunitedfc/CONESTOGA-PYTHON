#This program aim to build cars based on user input
#It will also act as a customization agent, which will 
#Get input from users for their desired upgrades/build

#---Input Check---
def stringCheck(input):
    if input.isdigit() is False and input!="":
        valid = True
    else:
        print(f"Invalid Input")
        valid = False
    return valid
def digitCheck(input):
    if input.isdigit() and input!="":
        valid = True
    else:
        print(f"Invalid Input")
        valid = False
    return valid

#Introduce to User Program Goal
print(f"Hello, this Program will help create your dream car lot")

#Create Car Class with User Info 
class Car:
    def __init__(self,make,model,trim,year,colour,drivetrain,mileage):
        #instance attributes
        self.make = make
        self.model = model
        self.trim = trim
        self.year = year
        self.colour = colour
        self.drivetrain = drivetrain
        self.mileage = mileage








# GET USER CAR
