"""
Title: Cipher function
Name: Ayan A.
Date: 21/07/2021
Description: A function that performs a simple moving cipher.
Given a key, the function shifts each letter in a message that many places.
"""


import string as s

def cipher(message: str, key: int):
    continuous_alphabet: str = s.ascii_lowercase * 999
    new_message = ''
    for letter in message:
        index: int = continuous_alphabet.find(letter)
        new_index: int = index + key
        new_message: str = continuous_alphabet[new_index]
    return new_message
