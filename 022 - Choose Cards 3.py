N = int(input())
A = list(map(int, input().split()))

answer = 0
for i in range(0, N):
	for j in range(i + 1, N):
		if A[i] + A[j]== 100000:
			answer += 1

# ?o??
print(answer)
