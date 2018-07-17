val=input()
val=val.split()
v1=int(val[0])
v2=int(val[1])
list1=[]
for i in range(v1+1,v2):
	if(i%2!=0):
		list1.append(i)
str1=""
for i in list1:
	str1=str1+" "+str(i)
print(str1[1:])
