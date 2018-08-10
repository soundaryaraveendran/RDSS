n1=int(input())
num=input()
num=num.split()
xy=[]
for i in range(n1):
	xy.append(int(num[i]))
x=(sorted(xy))
str1=""
for i in x:
    str1=str1+" "+str(i)
print(str1[1:])
