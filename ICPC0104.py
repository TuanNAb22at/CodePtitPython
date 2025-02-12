
n=int(input())
while n>0:
    s=input()
    d = 0
    m = 10 ** 20
    check = False
    for i in range(len(s)):
        if s[i] >= '0' and s[i] <= '9':
            d=d*10+int(s[i])
            check= True
        elif check == True:
            m=min(m,d)
            d=0
            check = False
    if(s[len(s)-1] >='0' and s[len(s)-1] <='9'): m=min(m,d)
    print(m)
    n=n-1