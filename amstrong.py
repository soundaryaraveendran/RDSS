num=int(input())
sum1=0
temp=num
while temp>0:
    dig=temp%10
    sum1 += dig **3
    temp//=10
if num==sum1:
    print("yes")
else:
    print("no")
