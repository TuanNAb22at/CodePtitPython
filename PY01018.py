
while True:
    line = input()
    if line == '0':break
    k,s=line.split()
    k=int(k)
    res=''
    p="ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    for i in s:
        index=p.find(i)
        res+=p[(index+k)%28]
    res=res[::-1]
    print(res)