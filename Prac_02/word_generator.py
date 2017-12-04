"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import string
import random


VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
BOTH = string.ascii_lowercase

word_format = str(input("Please provide a word format: "))
word = ""
for kind in word_format:
    if kind == "%":
        word += random.choice(CONSONANTS)
    elif kind == "c":
        word += random.choice(CONSONANTS)
    elif kind == "#":
        word += random.choice(VOWELS)
    elif kind == "v":
        word += random.choice(VOWELS)
    elif kind == "*":
        word += random.choice(BOTH)
    else:
        word += kind
print("Word Generated: ", word)
print("\n")

SPECIAL_CHARACTERS = "!#*"


rand_word_format_length = random.randint(5, 10)
rand_word_format = ""
for loop in range(rand_word_format_length, 0, -1):
    rand_word_format_char = str(random.choice(string.ascii_lowercase + SPECIAL_CHARACTERS))
    rand_word_format += rand_word_format_char
print("Randomly Generated Word Format: ", rand_word_format)
print("Length of Random Word Format: ", rand_word_format_length)

rand_word = ""

for kind_2 in rand_word_format:
    if kind_2 == "%":
        rand_word += random.choice(CONSONANTS)
    elif kind_2 == "c":
        rand_word += random.choice(CONSONANTS)
    elif kind_2 == "#":
        rand_word += random.choice(VOWELS)
    elif kind_2 == "v":
        word += random.choice(VOWELS)
    elif kind_2 == "*":
        rand_word += random.choice(BOTH)
    else:
        rand_word += kind_2
print("Word Generated: ", rand_word)