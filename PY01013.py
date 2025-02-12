import math

prime = [True]*(10**2+1)

def Prime():
    prime[0] , prime[1]= False,False
    for i in range(2,(int)(math.sqrt(10**2))+1):
        if prime[i]:
            for j in range(i*i,10**2+1,i):
                prime[j] = False

if __name__ == "__main__":
    Prime()
    t=int(input())
    for i in range(t):
        a,b=map(int,input().split())
        d=math.gcd(a,b)
        d=str(d)
        k=0
        for i in range(len(d)):
            k+=int(d[i])
        if(prime[k]):
            print("YES")
        else:
            print("NO")