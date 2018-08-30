num=input()
num=num.split()
list1=[]
for i in range(0,10):
	list1.append(int(num[i]))
print(max(list1))
