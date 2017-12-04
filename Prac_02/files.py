"""
1. Write a program that asks the user for their name, then opens a file called “name.txt” and writes that
name to it.
2. Write a program that opens “name.txt” and reads the name (as above) then prints,
“Your name is Bob” (or whatever the name is in the file).
3. Create a text file called “numbers.txt” (You can create a simple text file in PyCharm with Ctrl+N, choose
“File” and save it in your project). Put the numbers 17 and 42 on separate lines in the file and save it:
17
42
Write a program that opens “numbers.txt”, reads the numbers and adds them together then prints the
result, which should be… 59.
4. Extended (perhaps only do this if you’re cruising… if you are struggling, just read the solution) …
Now extend your program so that it can print the total for a file containing any number of numbers.
"""

name_file = open("Name.txt", 'w')
name = str(input("Please Enter Your Name: "))
print("Your name is {}".format(name), file=name_file)
name_file.close()

numbers_file = open("Numbers.txt", 'w')
number_1 = 17
number_2 = 42
print(number_1, "\n", number_2, file=numbers_file)
numbers_file.close()

from_numbers_file = open("Numbers.txt", 'r')
from_file_1 = int(from_numbers_file.readline())
from_file_2 = int(from_numbers_file.readline())
print(from_file_1+from_file_2)

extended = open("Numbers_extended.txt", 'r')
total=0
for line in extended:
    ext = int(line)
    total += ext
print(total)
extended.close()