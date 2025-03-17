import math
N,M=map(int, input().split())

a=N-M


def factorial_math(n):
    return math.factorial(n)
#M!
M=factorial_math(M)
#a!

a=factorial_math(a)
#n

n=factorial_math(N)
aa=M*a

answer=n/aa

print(int(answer))