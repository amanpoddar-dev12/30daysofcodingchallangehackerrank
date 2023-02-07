import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input().strip())
    # binary=bin(n).replace("0b", "")
    # print(binary)
    # length=(len(str(binary)))
    # print(length)  
    # c=0
    # for i in range(length):
        
    #     if  
    #         c=c+1
    #     else:
    #         break
    # print('number of time 1 ',c)
    
    binary = bin(n)[2:].split('0')
    # binary1 = bin(n)[2:]
    max = 0
    for i in binary:
    #  print(i)
     if len(i) > max:
       max = len(i)
    print(binary)
    print(max)
    
    # print(binary1)