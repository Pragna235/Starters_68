# cook your dish here
for t in range(int(input())):
    a,c=map(int,input().split())
    if((c-a )% 2==0):
        print((c+a)//2)
    else:
        print(-1)