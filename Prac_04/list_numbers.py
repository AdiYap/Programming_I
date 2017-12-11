"""Write a program that prompts the user for 5 numbers and then stores each of these in a list called
numbers. The program should then output various interesting things, as in the output below (green
represents user input).

Note that you can use the functions min, max, sum and len, and you can use the append method to
add a number to a list.

    Number: 5
    Number: 20
    Number: 1
    Number: 2
    Number: 3

The first number is 5
The last number is 3
The smallest number is 1
The largest number is 20
The average of the numbers is 6.2
"""

list_of_num = []

for i in range(5):
    num = int(input("Number: "))
    list_of_num.append(num)

print("The first number is {}".format(list_of_num[0]))
print("The last number is {}".format(list_of_num[-1]))
print("The smallest number is {}".format(min(list_of_num)))
print("The largest number is {}".format(max(list_of_num)))
print("The average of the numbers is {}".format(sum(list_of_num)/len(list_of_num)))