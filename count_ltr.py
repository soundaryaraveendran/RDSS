num=raw_input()
num=num.split()
count=0
for i in num:
    list1=list(i)
    count=count+len(list1)
print(count)
