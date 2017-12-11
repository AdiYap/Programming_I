"""Quick Pick Lottery Ticket Generator

Write a program that asks the user how many “quick picks” they wish to generate. The program then
generates that many lines of output. Each line consists of 6 random numbers between 1 and 45. These
values should be stored as CONSTANTS.

Each line should not contain any repeated number. Make sure your numbers are unique.
Each line of numbers should be displayed in sorted (ascending) order.
Note: Python's random function has a sample method, which returns a selection from a list. This is a
nice way to solve this problem... but it's too easy :) Do not use it for this program.
Your code should produce output that matches this sample output (except the numbers are random):

How many quick picks? 5
9 10 11 32 38 44
2 9 12 14 28 30
5 10 16 22 35 42
1 2 16 22 37 40
1 17 20 23 25 27
"""


import random


rows = 6
min_pick = 1
max_pick = 45

def Main():
    valid_input = False
    while not valid_input:
        try:
            no_of_picks = int(input("How many Quick Picks? "))
            if no_of_picks <= 0:
                print("Value cannot be 0 or less!")
                valid_input = False
            else:
                valid_input = True
        except ValueError:
            print ("Invalid Input!")


    for picks in range(1, no_of_picks + 1):
        quick_pick = []
        for numbers in range(rows):
            generated_row = random.randint(min_pick,max_pick)
            quick_pick.append(generated_row)
        print(" ".join("{:2}".format(picks) for picks in quick_pick))

Main()