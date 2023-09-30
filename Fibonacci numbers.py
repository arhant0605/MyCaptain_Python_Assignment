# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 20:22:13 2023

@author: hp
"""

def genrate_fibonacci(n):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence[:n]   

n_terms = 10
fibonacci_result = genrate_fibonacci(n_terms)
print(f"The first {n_terms} Fibonacci numbers are: {fibonacci_result}")


        