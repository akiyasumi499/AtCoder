N, S = map(int, input().split())
A = list(map(int, input().split()))

answer = 'No'
def compareS(sum, n):
    for i in range(n, N):
        global answer
        if answer == 'Yes': break

        temp = sum + A[i]
        if temp > S: continue
        if temp == S:
            answer = 'Yes'
            break
        if i + 1 < N: compareS(temp, i + 1)

compareS(0, 0)
print(answer)