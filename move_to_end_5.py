"""
Title: Moving function
Name: Ayan A.
Date: 21/07/2021
Description: A function that moves a certain element to the end of an array, inplace.
"""


def move_to_end(array: list, toMove: int):
    index: int = 0
    counter: int = 0
    while counter < len(array):
        if array[index] == toMove:
            pop: int = array.pop[index]
            array.append(pop)
            counter += 1
        else:
            index += 1
            counter += 1
    return array
