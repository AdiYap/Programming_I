

lower = 33
upper = 127


def Main():
    char = input("Enter a character: ")
    print("The ASCII code for {} is {}".format(char, ord(char)))
    number = get_number(lower,upper)
    print("The character for {} is {}".format(number, chr(number)))


    """for value in range(lower, upper + 1):
        print("{:3} {:>4}".format(value, chr(value)))"""


def get_number(lower,upper):
    valid_input = False
    #ensure user input is valid
    while not valid_input:
        try:
            print("Enter a number ({} - {}): ".format(lower, upper))
            number = int(input(">>>"))
            while number < lower or number > upper:
                print("Please enter a Valid Number!")
                print("Enter a number ({} - {}): ".format(lower, upper))
                number = int(input(">>>"))
            valid_input = True
        except ValueError:
            print ("Please enter a Valid Number!")
    return number

Main()




