#!/usr/bin/python3
import sys

# Function description:
# This function calculates the factorial of a given number n recursively.
# A factorial of a number n (denoted as n!) is the product of all positive integers less than or equal to n.
# The factorial of 0 is defined as 1.
#
# Parameters:
# n (int): The number for which we want to calculate the factorial. 
# It must be a non-negative integer (n >= 0).
#
# Returns:
# int: The factorial of the number n. 
# If n is 0, the function returns 1. Otherwise, it returns n * (n-1) * ... * 1 recursively.

def factorial(n):
    # Base case: if n is 0, return 1
    if n == 0:
        return 1
    else:
        # Recursive case: return n multiplied by the factorial of (n-1)
        return n * factorial(n-1)

# The main program block
# Convert the first command-line argument to an integer and call the factorial function
# sys.argv[1] is the first argument passed from the command line (after the script name)
f = factorial(int(sys.argv[1]))

# Output the result (factorial)
print(f)
