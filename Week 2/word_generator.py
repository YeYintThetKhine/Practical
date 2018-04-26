import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

print("Please enter a word format.\nUse 'c' for consonants or 'v' for vowels.")
word_format = input("Word format: ")

word = ""

for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
else:
    word += random.choice(VOWELS)

print(word)
