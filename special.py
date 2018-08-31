value=input()
value=list(value)
count=0
string="!@#$%^&*()_+.,<>/?"
string=list(string)
for i in value:
    if i in string:
        count=count+1
print(count)
