num=input()
num=num.split()
xy=[]
for i in range(3):
	xy.append(int(num[i]))
print(max(xy))
