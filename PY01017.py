
t=int(input())
for i in range(t):
    s=input()
    count = 1
    res=""
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            res+=str(count) + s[i - 1]
            count = 1
    res+=str(count) + s[len(s) - 1]
    print(res)