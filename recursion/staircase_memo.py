# uses memoization ; O(n) solution
import math
import os
import random
import re
import sys

# Complete the stepPerms function below.

    
def stepPerms(n, memo):
    if n<=1:
        memo[n] = 1
    elif n==2:
        memo[n] = 2
    elif n==3:
        memo[n]= 4
    else:
        if memo[n]==0:
            memo[n]= stepPerms(n-1, memo)+ stepPerms(n-2, memo)+ stepPerms(n-3, memo)
    return memo[n]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())
        memo = [0]*(n+1)

        res = stepPerms(n, memo)

        fptr.write(str(res) + '\n')

    fptr.close()