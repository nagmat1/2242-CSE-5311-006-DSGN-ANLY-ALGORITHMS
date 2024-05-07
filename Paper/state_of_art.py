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
    oper1 = 0
    A = sorted(A)
    print("k = {}  , A={} ".format(k, A))
    for i in range(len(A)):
        if A[i] >= k:
            break
    print(" i = {} A[i]={},k={}".format(i,A[i],k))
    A2 = A[i+1:]
    if A[i] < k:
        A3 = A[:i + 1]
    else:
        A3 = A[:i]
    #print("==k = {}  , A3={} A2 = {} ".format(k, A3, A2))
    while len(A3) > 0:
        if len(A3) < 2:
            oper1 = oper1 + 1
            break
        else:
            new_val = A3[0] + 2 * A3[1]
            oper1 = oper1 + 1
        if new_val >= k:
            A2.append(new_val)
            A3 = A3[2:]
        else:
            A3.append(new_val)
            A3 = sorted(A3)
            if len(A3) == 1:
                oper1 = oper1 + 1
            else:
                A3 = A3[2:]
        #print("k = {}  , A3={} A2 = {} oper1 = {} ".format(k, A3, A2, oper1))
    if len(A2) < 1:
        return -1
    return oper1

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
