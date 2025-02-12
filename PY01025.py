
s=input()
cnt=len(s)%3
res=''
if cnt!=0:
    for i in range(0,cnt):
        print(s[i],end='')
    if len(s)>3 : print(",",end='')
dem=0
for i in range(cnt,len(s),1):
    dem=dem+1
    print(s[i], end="")
    if dem % 3 == 0 and i != len(s)-1:
        print(",", end='')