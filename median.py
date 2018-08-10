import math

n1=int(input())
num=input()
num=num.split()
xy=[]
for i in range(n1):
	xy.append(int(num[i]))
x=(sorted(xy))
l=len(x)
f=math.ceil(l/2)
print(x[f-1])
