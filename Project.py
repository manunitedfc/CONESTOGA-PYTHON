#This program aim to build cars based on user input
#It will also act as a customization agent, which will 
#Get input from users for their desired upgrades/build
#import copy
import copy
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
    def carPrint(self,fh=None):
        if fh is not None:
            print(f"Car Make: {self.make}",file=fh)
            print(f"Car Model: {self.model}",file=fh)
            if self.trim is not None:
                print(f"Car Trim: {self.trim}",file=fh)
            print(f"Car Year: {self.year}",file=fh)
            print(f"Car Colour: {self.colour}",file=fh)
            print(f"Car Drivetrain: {self.drivetrain}",file=fh)
            print(f"Car Mileage: {self.mileage}",file=fh)
        else:
            print(f"Car Make: {self.make}")
            print(f"Car Model: {self.model}")
            if self.trim is not None:
                print(f"Car Trim: {self.trim}")
            print(f"Car Year: {self.year}")
            print(f"Car Colour: {self.colour}")
            print(f"Car Drivetrain: {self.drivetrain}")
            print(f"Car Mileage: {self.mileage}")


#New line
print()
# GET USER CAR FUNCTION
def getuserCar(fh=None):
    valid = False
    #Get User Input
    while valid is False:
        while valid is False:
            make = str(input("Enter Make: ").strip().capitalize())
            if stringCheck(make) is False:
                break
            model = str(input("Enter Model: ").strip().capitalize())
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
            carobject = Car(make,model,trim,year,colour,drivetrain,mileage)
            return carobject

#GET USER PACKAGE CHOICES

def getuserCustomizations(fh=None):
    valid = False
    #Get User Input
    while valid is False:
        while valid is False:
            premiumAudio = str(input("Premium Audio Package? (y/n): ").strip().upper())
            #check input
            match premiumAudio:
                case "Y":
                    None
                case "N":
                    premiumAudio = None
                case _:
                    print(f"Invalid Input")
                    break
            premiumMedia = str(input("Upgraded Infotainment Screen? (y/n): ").strip().upper())
            match premiumMedia:
                case "Y":
                    None
                case "N":
                    premiumMedia = None
                case _:
                    print(f"Invalid Input")
                    break
            premiumLights = str(input("Halogen Headlights? (y/n): ").strip().upper())
            match premiumLights:
                case "Y":
                    None
                case "N":
                   premiumLights = None
                case _:
                    print(f"Invalid Input")
                    break
            premiumSeats = str(input("Premium Leather Seats? (y/n): ").strip().upper())
            match premiumSeats:
                case "Y":
                    None
                case "N":
                    premiumSeats = None
                case _:
                    print(f"Invalid Input")
                    break
            remoteStart = str(input("Remote Start? (y/n): ").strip().upper())
            match remoteStart:
                case "Y":
                    None
                case "N":
                    remoteStart = None
                case _:
                    print(f"Invalid Input")
                    break
            valid = True
    return [premiumAudio,premiumMedia,premiumLights,premiumSeats,remoteStart]

#Print Package Methods
def printPackage(userCustomization,fh=None):
    if fh is not None:
        print(f"Car Packages\n",file=fh)
        if userCustomization[0] is not None:
            print("Premium Audio Package",file=fh)
        if userCustomization[1] is not None:
            print("Upgraded Infotainment Screen",file=fh)
        if userCustomization[2] is not None:
            print("Halogen Headlights",file=fh)
        if userCustomization[3] is not None:
            print("Premium Leather Seats",file=fh)
        if userCustomization[4] is not None:
            print("Remote Start ",file=fh)
    else:
        print(f"Car Packages\n")
        if userCustomization[0] is not None:
            print("Premium Audio Package")
        if userCustomization[1] is not None:
            print("Upgraded Infotainment Screen")
        if userCustomization[2] is not None:
            print("Halogen Headlights")
        if userCustomization[3] is not None:
            print("Premium Leather Seats")
        if userCustomization[4] is not None:
            print("Remote Start ")


#Ask until user stops
def userContinue():
    j= False
    while j == False:
        while j == False:
            userSatisfied = str(input("\nAdd another car? (y/n): ").strip().upper())
            print()
            match userSatisfied:
                case "Y":
                    j =  True
                    userSatisfied = False
                case "N":
                    j = True
                    userSatisfied = True
                case _:
                    print("Invalid Input")
                    break
    return userSatisfied

#GET FIRST CAR
carLot = []
carLot.append([getuserCar(),getuserCustomizations()])

#Check For User Continue
userSatisfied = userContinue()
while userSatisfied == False:
    carLot.append([getuserCar(),getuserCustomizations()])
    userSatisfied = userContinue()
    

#---OUTPUT---

#print to file (user choice)
def userfileChoice():
    j= False
    while j == False:
        while j == False:
            printOption = str(input("\nPrint to File? (y/n): ").strip().upper())
            print()
            match userSatisfied:
                case "Y":
                    j =  True
                    printOption = False
                case "N":
                    j = True
                    printOption = True
                case _:
                    print("Invalid Input")
                    break
    return printOption
printOption = userfileChoice()


#Print to user/file

#get file handle if needed
if printOption == True:
    try:
        newFile = open("Cars.txt",'x')
        newFile.close()
        fh = open("Cars.txt","a")
        fh.write("Your CARS:\n")
    except:
        fh = open("Cars.txt","a")
        fh.write("YOUR CARS:\n")
else:
    fh = None
#print/write user car data
i= 1
for car in carLot:
    print(f"---CAR {i}---\n")
    car[0].carPrint(fh)
    printPackage(car[1],fh)

