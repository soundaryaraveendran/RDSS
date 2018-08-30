string=input()
string1=list(string)
count=0
for i in string1:
    if i.isdigit():
        count=count+1
print(count)
