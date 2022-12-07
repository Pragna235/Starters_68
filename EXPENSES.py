# cook your dish here
for t in range(int(input())):
    n,x=map(int,input().split())
    total=(2**x)
    for i in range(1,n+1):
        total=total//2
    print(total)