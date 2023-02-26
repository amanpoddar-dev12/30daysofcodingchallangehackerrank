#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())

    names = []

    for N_itr in range(N):
            first_multiple_input = input().rstrip().split()

            firstName = first_multiple_input[0]

            emailID = first_multiple_input[1]

                # if emailID.endswith("@gmail.com"):
            if re.match(r'.*@gmail.com$', emailID):
                     names.append(firstName) 

    print(*sorted(names),sep="\n")
    
