string=input()
string1=list(string)
count=0
list1="!@#$%^&*()_+.,><?/"
list2=list(list1)
for i in string1:
    if i in list2:
        count=count+1
print(count)

