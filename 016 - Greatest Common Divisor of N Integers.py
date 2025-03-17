def gcd(A, B):
    while A >= 1 and B >= 1:
        if A < B:
            B = B % A
        else:
            A = A % B
    if A >= 1:
        return A
    return B


N = int(input())
A = list(map(int, input().split()))
cur = A[0]
for i in range(1, N):
    cur = gcd(cur, A[i])

print(cur)