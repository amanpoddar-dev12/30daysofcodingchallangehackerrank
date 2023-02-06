
count=int(input())
dictonar={}
for i in range(count):
    data=input().split()
    dictonar[data[0]]=data[1]
while True:
    try:
        name = input()
        if name in dictonar:
            print(name + "=" + dictonar[name])
        else:
            print("Not found")
    except EOFError:
        break
        
    