#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    from heapq import heappop, heappush, heapify
    oper1 = 0
    cookies= A
    minSweetness = k
    heapify(cookies)

    fC = 0
    try:
        while cookies[0] < minSweetness:
            fC += 1
            c1 = heappop(cookies)
            c2 = heappop(cookies)
            newCookie = (1 * c1) + (2 * c2)
            heappush(cookies, newCookie)
        return fC
    except:
        return -1

    # Write your code here


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    file1 = open("test26.txt", "r")

    first_multiple_input = file1.readline()
    n, k = first_multiple_input.rstrip().split()
    n= int(n)
    k = int(k)
    print("Input = {} n = {} k = {} ".format(first_multiple_input,n,k))
    values = file1.readline()
    A = list(map(int, values.rstrip().split()))
    print("Input = {} A = {} ".format(values, A))

    result = cookies(k, A)
    print("Result = {} \n".format(result))
