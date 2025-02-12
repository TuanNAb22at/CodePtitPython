

def count(a,n):
    d=0
    a.sort()
    for i in range(0,n-2):
        l,r=i+1,n-1
        while l<r:
            sum=a[l]+a[r]+a[i]
            if sum==0:
                d=d+1
                l+=1
            elif sum>0:
                r=r-1
            else:
                l=l+1
    return(d)

t=int(input())
while(t>0):
    n=int(input())
    a=list(map(int,input().split()))
    print(count(a,n))
    t=t-1

