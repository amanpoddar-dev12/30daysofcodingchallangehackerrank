# https://www.hackerrank.com/challenges/30-sorting/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys



n = int(input().strip())
a = list(map(int, input().rstrip().split()))
 
# Write your code here
numSwaps=0
for i in range(0,n):
    numberOfSwaps=0
    for j in range(0,n-1):
        if (a[j] > a[j + 1]):
            s=a[j]
            a[j]=a[j + 1]
            a[j+1]=s
            numberOfSwaps=numberOfSwaps+1
    if numberOfSwaps==0:
        break
    else:
        numSwaps+=numberOfSwaps
        
print('Array is sorted in',numSwaps,'swaps.')
print('First Element:',a[0])
print('Last Element:',a[-1])
        
    
    
    
    
    
    
            
                 
               
