MENU = """
-----*-----
This program will calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
-----*-----

Press 'A' to begin.
Press 'Q' to Quit.
"""
print(MENU)
choice = input(">>> ")
while choice != "Q":
    if choice == "A":
        valid_input = False
        #This value is used to check if the input is valid
        while not valid_input:
            try:
                sales = float(input("Please Enter User Sales: $"))
                valid_input = True
                #If the input is valid, it will become true.
                #This line will only be called if the previous line does not return an error
            except ValueError:
                print("Invalid Input")
            else:
                while sales < 0:
                    print("Invalid Amount")
                    sales = float(input("Please Enter User Sales: $"))
                if sales < 1000:
                    bonus = (sales / 100)*10
                    print("Bonus received: $ {:.2f}".format(bonus))
                    print("Please try harder next time.")
                    print("Press A to continue, or Q to quit")
                elif sales >= 1000:
                    bonus = (sales / 100)*15
                    print("Bonus received: $ {:.2f}".format(bonus))
                    print("Good Work! Keep it up!")
                    print("Press A to continue, or Q to quit")
    elif choice != "A":
        print("Invalid Option")
    choice = input(">>>")
print("Thank you.")
exit(0)

