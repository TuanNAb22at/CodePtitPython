
stack = []
n=int(input())
a=list(map(int,input().split()))
for i in range(len(a)):
    if(len(stack) == 0):
        stack.append(a[i])
    else:
        if((stack[len(stack)-1] + a[i] )%2 !=0):
            stack.append(a[i])
        elif len(stack) > 0:
            stack.pop();
print(len(stack))







