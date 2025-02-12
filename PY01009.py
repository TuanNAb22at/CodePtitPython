s=input()
t,h=0,0
for i in s:
    if i.isupper(): h=h+1
    if i.islower(): t=t+1
if t>=h:
    print(s.lower())
if h>t:
    print(s.upper())