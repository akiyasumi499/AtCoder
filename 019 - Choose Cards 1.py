import math

N = int(input())
A = list(map(int,input().split()))

ls = [A.count(i) for i in range(1,4)]
print(sum([math.comb(ls[i],2) for i in range(3)]))