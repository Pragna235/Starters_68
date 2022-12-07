# cook your dish here
for t in range(int(input())):
    n,x,c=map(int,input().split())
    a=list(map(int,input().split()))
    sum1,count=0,0
    
    #print(arr)
    for i in range(n):
        if(x-a[i]>c):
            sum1+=x 
            count+=c 
        else:
            sum1+=a[i]
    print(sum1-count)
    