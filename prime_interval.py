val=input()
val=val.split()
lower = int(val[0])
upper = int(val[1])
list1=[]
for num in range(lower,upper + 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           list1.append(num)
str1=""
for i in list1:
    str1=str1+str(i)+" "
print(str1)
