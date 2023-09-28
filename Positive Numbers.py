# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 02:33:24 2023

@author: hp
"""

def print_positive_numbers(input_list):
    positive_numbers=[]
    for num in input_list:
        if num > 0:
            positive_numbers.append(num)
            
    print("Input:",input_list)
    print("Output:",positive_numbers)
            
            
list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]

print_positive_numbers(list1)
print_positive_numbers(list2)
           