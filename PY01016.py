

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        s=input()
        for j in range(1,len(s)):
            if s[j] >='0' and s[j] <='9':
                d=int(s[j])
                for k in range(0,d):
                    print(s[j-1],end="")
        print()