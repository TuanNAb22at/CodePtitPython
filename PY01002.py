import math
from math import *


if __name__ == "__main__":
    a,b,c,d,e=input().split()
    a,c,e = int(a),int(c),int(e)
    if a+c == e:print("YES")
    else:print("NO")