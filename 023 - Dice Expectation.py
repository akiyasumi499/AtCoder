N = int(input())
B = list(map(int, input().split()))
R = list(map(int, input().split()))

blue = 0.0
red = 0.0
for i in range(N):
	blue += B[i] / N
	red += R[i] / N

# o—Í
print("%.12f" % (blue + red))
