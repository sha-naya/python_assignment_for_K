"""
Title: Palindrome function
Name: Ayan A.
Date: 21/07/2021
Description: A function that return True if a string is a palindrome, False otherwise.
"""


def palindrome(word: str):
    if word == word[::-1]:
        return True
    else:
        return False
