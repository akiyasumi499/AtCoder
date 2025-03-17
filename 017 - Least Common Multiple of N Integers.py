n=int(input())
a=list(map(int,input().split()))
from math import gcd
g=a[0]
for i in range(n):
  g=(g*a[i])//gcd(g,a[i])
print(g)