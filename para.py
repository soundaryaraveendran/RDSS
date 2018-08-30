string=input()
string1=list(string)
count=1
for i in string1:
    if i==".":
        count=count+1
print(count)
