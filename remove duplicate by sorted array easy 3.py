list1=[1,1,2,3,3,5,5,]
l=[]
for i in list1:
    if list1[i] not in l:
        l.append(list1[i])
print(l)