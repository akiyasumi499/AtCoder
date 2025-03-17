N =int(input())
A = list(map(int, input().split()))


a100=A.count(100)
a200=(A.count(200))
a300=(A.count(300))
a400=(A.count(400))

aa=a100*a400
bb=a200*a300
aaa=aa+bb
print(aaa)