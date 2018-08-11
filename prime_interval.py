num=input()
num=num.split()
lower=int(num[0])
upper=int(num[1])
str1=""
for i in range(lower,upper+1):
	if i>1:
		for j in range(2,i):
			if((i%j)==0):
				break
		else:
			str1=str1+str(i)+" "
print(str1)
