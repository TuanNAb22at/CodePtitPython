
def func(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            cnt=0
            while(n%i==0):
                cnt+=1
                n=n/i
            print(" * ",i,"^",cnt,end="",sep="")
    if n > 1:
        print(" * ",int(n),"^1",end="",sep="")


if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        print("1",end="")
        func(n)
        print()