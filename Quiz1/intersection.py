a=[1,2,3,4]
b=[1,5,3,6]
new_list=[]

for i in b:
    if i not in a:
        new_list.append(i)
print(new_list)