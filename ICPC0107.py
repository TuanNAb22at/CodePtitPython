
def tong_min (s1,s2,d1,d2):
    k1=''
    k2=''
    for i in range(len(s1)):
        if(s1[i] == d2+''):
            k1=k1+(d1+'')
        else: k1=k1+s1[i]

    for i in range(len(s2)):
        if (s2[i] == d2 + ''):
            k2 = k2 + (d1 + '')
        else:
            k2 = k2 + s2[i]
    return int(k1)+int(k2)

def tong_max (s1,s2,d1,d2):
    k1=''
    k2=''
    for i in range(len(s1)):
        if(s1[i] == d1+''):
            k1=k1+(d2+'')
        else: k1=k1+s1[i]

    for i in range(len(s2)):
        if (s2[i] == d1 + ''):
            k2 = k2 + (d2 + '')
        else:
            k2 = k2 + s2[i]
    return int(k1)+int(k2)
if __name__ == '__main__':
    t=int(input())
    while t>0:
        n,m=input().split()
        s=input()
        k=input()
        d1=min(n,m)
        d2=max(n,m)
        print(tong_min(s,k,d1,d2),tong_max(s,k,d1,d2))
        t=t-1