import random
import string

Character_Pool = "" #Contains all the Characters to be selected by the code at random

#
#
#
#Queries User for Length of Password, Checks if input is valid
Valid_Pass_Length = False
while not Valid_Pass_Length:
    try:
        Password_Length = int(input("How long should this password be? (Must not be less than 5 or more than 15)"))
        if Password_Length < 5:
            Valid_Pass_Length = False
            print("Password is too short!")
        elif Password_Length > 15:
            Valid_Pass_Length = False
            print("Password is too long!")
        else:
            Valid_Pass_Length = True
    except ValueError:
        print("Invalid Length!")
print("Length of Password: ", Password_Length)
#
#
#
#
#
#
#Queries if User wants to include Uppercase Characters, Checks if input is valid
Valid_Input_Upper = False
while not Valid_Input_Upper:
    try:
        Uppercase = str(input("Should your password contain Uppercase Characters? (Y/N)"))
        if Uppercase is "Y":
            Character_Pool += string.ascii_uppercase    #Adds Uppercase Characters to the Pool
            Valid_Input_Upper = True
        elif Uppercase is "N":
            Valid_Input_Upper = True
        else:
            Valid_Input_Upper = False
            print("Invalid Input! Please indicate with either Y or N")
    except ValueError:
        print("Invalid Input! Please indicate with either Y or N")
print("Contains Uppercase: ", Uppercase)
#
#
#
#
#
#
#Queries if User wants to include Lowercase Characters, Checks if input is valid
Valid_Input_Lower = False
while not Valid_Input_Lower:
    try:
        Lowercase = str(input("Should your password contain Lowercase Characters? (Y/N)"))
        if Lowercase is "Y":
            Character_Pool += string.ascii_lowercase    #Adds Lowercase Characters to the Pool
            Valid_Input_Lower = True
        elif Lowercase is "N":
            Valid_Input_Lower = True
        else:
            Valid_Input_Lower = False
            print("Invalid Input! Please indicate with either Y or N")
    except ValueError:
        print("Invalid Input! Please indicate with either Y or N")
print("Contains Lowercase: ", Lowercase)
#
#
#
#
#
#
#Queries if User wants to include Numbers, Checks if input is valid
Valid_Input_Numbers = False
while not Valid_Input_Numbers:
    try:
        Numbers = str(input("Should your password contain Numbers Characters? (Y/N)"))
        if Numbers is "Y":
            Character_Pool += string.digits     #Adds Numbers to the Pool
            Valid_Input_Numbers = True
        elif Numbers is "N":
            Characters_Num = ""
            Valid_Input_Numbers = True
        else:
            Valid_Input_Numbers = False
            print("Invalid Input! Please indicate with either Y or N")
    except ValueError:
        print("Invalid Input! Please indicate with either Y or N")
print("Contains Numbers: ", Numbers)
#
#
#
#
#
#
#Queries if User wants to include Special Characters, Checks if input is valid
Valid_Input_Special = False
while not Valid_Input_Special:
    try:
        Special = str(input("Should your password contain Special Characters? (Y/N)"))
        if Special is "Y":
            Character_Pool += "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"      #Adds Special Characters to the Pool
            Valid_Input_Special = True
        elif Special is "N":
            Valid_Input_Special = True
        else:
            Valid_Input_Special = False
            print("Invalid Input! Please indicate with either Y or N")
    except ValueError:
        print("Invalid Input! Please indicate with either Y or N")
print("Contains Special Characters: ", Special)


Rand_Password = ""
for loop in range(Password_Length,0,-1):
    Rand_Password += random.choice(Character_Pool)      #Selects Random Values from the Pool
print(Rand_Password)