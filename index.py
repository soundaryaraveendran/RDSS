num=int(input())
numbers=raw_input()
numbers=numbers.split()
list1=[]
for i in range(0,num):
    list1.append(int(numbers[i]))
for i in list1:
    str1=""
    str1=str(i)+" "+str(list1.index(i))
    print(str1)
