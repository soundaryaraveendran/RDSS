n1=int(input())
num=input()
num=num.split()
xy=[]
for i in range(n1):
	xy.append(int(num[i]))
print(max(xy))
