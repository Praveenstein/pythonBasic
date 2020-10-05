# -*- coding: utf-8 -*-
""" Horner's method for polynomial evaluation

This script allows the user to evaluate a given polynomial in O(n) time
A polynomial 2x^2 + 3x -1 is given as a list of coefficients as: [2, 3, -1]

This file contains the following function:

    * main - the main function of the script

"""

from functools import reduce


def evaluate_polynomial():
    """
    Main function to evaluate the polynomial function
    """

    coefficients = [1, 0, 0, -1, -10]
    x = 2

    # The algorithm initializes result as coefficient of x^n, where n is the degree of polynomial and then
    # Repeatedly multiply result with x and add next coefficient to result
    result = reduce(lambda arg1, arg2: (arg1*x) + arg2, coefficients)

    print(f'The function evaluated to : {result} for given x value: {x}')


if __name__ == '__main__':
    evaluate_polynomial()
