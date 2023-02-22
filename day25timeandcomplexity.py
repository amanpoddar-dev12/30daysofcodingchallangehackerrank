# def prime(n):
#     if n==1:
#         print('Not prime')
#     else:
#         c=1
#         for i in range(1,int(n/2)+1):
#             if n%i==0:
#               c=c+1
#         if c==2:
#             print('Prime')
#         else:
#             print('Not prime')
# num=int(input())
# for i in range(1,num+1):
#     n=int(input())
#     prime(n)

from math import sqrt

def prime(N):
    check = "Prime"
    if N <= 1:
        check = "Not prime"
    else:
        for i in range(2,int(sqrt(N))+1):
            if N%i == 0:
                check = "Not prime"
                break
    return check

number = int(input())
for _ in range(number):
    N = int(input())
    print(prime(N))