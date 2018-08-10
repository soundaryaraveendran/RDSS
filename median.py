n1=int(input())
num=input()
num=num.split()
xy=[]
for i in range(n1):
	xy.append(int(num[i]))
x=(sorted(xy))
l=len(x)
print(x[l-2])
