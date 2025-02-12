
n=int(input())
while n>0:
    s=input()
    d = 0
    m = 0
    for i in range(len(s)):
        if s[i] >= '0' and s[i] <= '9':
            d=d*10+int(s[i])
            check= True
        else:
            m=max(m,d)
            d=0
    if(s[len(s)-1] >='0' and s[len(s)-1] <='9'): m=max(m,d)
    print(m)
    n=n-1