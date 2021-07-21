"""
Title: Palindrome function
Name: Ayan A.
Date: 21/07/2021
Description: A function that return True if a word is an isogram, False otherwise.
"""


def isogram(word: str):
    letter_holder: list = []
    for letter in word:
        if letter in letter_holder:
            return False
        else:
            letter_holder.append(letter)
    return True
