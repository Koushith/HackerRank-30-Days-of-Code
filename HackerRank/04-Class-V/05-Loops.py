"""
Objective
In this challenge, we're going to use loops to help us do some simple math. Check out the Tutorial tab to learn more.
Task
Given an integer, N, print its first 10 multiples.
Each multiple N * i (where 1 <= i <= 10) should be printed on a new line in the form:
N x i = result.
"""


import math
import os
import random
import re
import sys


if __name__ == '__main__':
    print("Input no")
    n = int(input())
for i in range(1, 11):
    print(str(n) + " x " + str(i) + " = " + str(N * i))
