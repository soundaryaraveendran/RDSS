va=input()
va=va.split()
l = int(va[0])
u = int(va[1])
list1=[]
for num in range(l,u + 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           list1.append(num)
str11=""
for i in list1:
    str11=str11+str(i)+" "
print(str11)
