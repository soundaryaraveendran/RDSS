num=int(input())
pdt=0
for x in range(1,num+1):
    if num%x==0:
        pdt=pdt+1
if pdt==2:
    print("yes")
else:
    print("no")
        
