N,S = map(int,input().split())
answer=0
for i in range(1,N+1):
    for j in range(1,N+1):
        if i+j<=S:
            answer=answer+1
print(answer)