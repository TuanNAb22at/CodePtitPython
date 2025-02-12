
def check(s):
    sum = 0
    for char in s:
        sum += int(char)
    if sum % 10 !=0 :
        return False
    for i in range(1,len(s)):
        if ( int(s[i])-2 != int(s[i-1])) and ( int(s[i]) != int(s[i-1])-2):
            return False
    return True


if __name__ == '__main__':
    for i in range(int(input())):
        s = input()
        if check(s):
            print("YES")
        else:
            print("NO")