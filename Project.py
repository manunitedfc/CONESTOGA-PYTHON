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
    def __init__(self,make,model,trim,year,colour,drivetrain,mileage,age):
        #instance attributes
        self.make = make
        self.model = model
        self.trim = trim
        self.year = year
        self.colour = colour
        self.drivetrain = drivetrain
        self.mileage = mileage
#New line
print()
# GET USER CAR

def getuserCar():
    valid = False
    #Get User Input
    while valid is False:
        while valid is False:
            make = str(input("Enter Make: ").strip().capitalize())
            if stringCheck(make) is False:
                break
            model = str(input("Enter Model: ").strip().capitalize)
            if stringCheck(model) is False:
                break
            trim = str(input("Enter Trim (or Blank): ").strip().upper())
            if trim == "":
                trim = None
            year = str(input("Enter Year: ").strip())
            if digitCheck(year) is False:
                break
            colour = str(input("Enter Colour: ").strip().capitalize())
            if stringCheck(colour) is False:
                break
            #Get Drivetrain
            print("\n1 - FWD\n2 - RWD\n3 - AWD\n")
            option = str(input("Enter Drivetrain Option (1/2/3): "))
            match option:
                case "1":
                    drivetrain = "FWD"
                case "2":
                    drivetrain = "RWD"
                case "3":
                    drivetrain = "AWD"
                case _:
                    break
            #Get Mileage
            mileage = str(input("Enter Desired Mileage (e.g., 1000): ").strip())
            if digitCheck(mileage) is False:
                break
            valid = True
            print()


getuserCar()




#print to file (user choice)