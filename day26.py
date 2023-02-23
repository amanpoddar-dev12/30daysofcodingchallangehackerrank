# Enter your code here. Read input from STDIN. Print output to STDOUTnb  
[[(lambda Fine: ((lambda Fine: print(Fine))(10000) if (Yr > Yd) else (((lambda Fine: print(Fine))(0) if (Mr < Md) else ((lambda Fine: print(Fine))(((Mr - Md) * 500)) if (Mr > Md) else (((lambda Fine: print(Fine))(((Dr - Dd) * 15)) if (Dr > Dd) else ((lambda Fine: print(Fine))(0) if (Dr == Dd) else (lambda Fine: print(Fine))(0))) if (Mr == Md) else print(Fine)))) if (Yr == Yd) else print(Fine))))(0) for (Dd, Md, Yd) in [map(int, input().split())]][0] for (Dr, Mr, Yr) in [map(int, input().split())]][0]
            
