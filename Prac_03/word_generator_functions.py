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
accepted = "cv"


word_format = ""
def is_valid_format(word_format):
    error_detect = 0
    for letter in word_format:
        if letter not in accepted:
            error_detect = error_detect + 1
    if error_detect >= 1:
        return False


while not is_valid_format(word_format):
    print("Please use only c and v")
    word_format = str(input("Please provide a word format: "))

word = ""
for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    elif kind == "v":
        word += random.choice(VOWELS)
print("Word Generated: ", word)
print("\n")
