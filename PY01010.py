
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=input()
        d1=(int)(s[len(s)-2]+s[len(s)-1])
        d2=(int)(s[0]+s[1])
        if d1==d2:
           print("YES")
        else:
           print("NO")