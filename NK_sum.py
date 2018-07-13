num=input()
num=num.split()
num1=int(num[0])
num2=int(num[1])
val=input()
val=val.split()
list1=[]
sum1=0
for i in range(num1):
	list1.append(int(val[i]))
for j in range(num2):
	sum1=sum1+list1[j]
print(sum1)
