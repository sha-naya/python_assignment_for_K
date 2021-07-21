"""
Title: "Special sum" function
Name: Ayan A.
Date: 21/07/2021
Description: A function that performs a special sum of its elements.
It follows the following logic - if array equals this [5, 2, [7, -1], 3, [6, [-13, 8], 4]] for instance,
then the output of the function is equal to 5 + 2 + 2 * (7 – 1) + 3 + 2 * (6 + 3 * (-13 + 8) + 4).
Contents of an array inside an array are multiplied by 2. Contents of an array inside an array inside
an array are multiplied by 3, and so on.
"""


from typing import Generator

def special_sum(special_array: list, depth: int = 1):
    integers: Generator = (element for element in special_array if isinstance(element, int))
    arrays: Generator = (element for element in special_array if isinstance(element, list))
    return depth * (sum(integers) + 
        sum(special_sum(special_array=element, depth = depth + 1) for element in arrays))
