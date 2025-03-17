A = list(map(int, input().split()))
summ=1
for i in range(len(A)):
    summ=A[i]*summ
print(summ)