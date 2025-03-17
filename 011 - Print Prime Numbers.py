N = int(input())
prime = [2]
for i in range(3, N + 1):
    for j in prime:
        if not i % j: break
    else:
        prime.append(i)

print(*sorted(prime))