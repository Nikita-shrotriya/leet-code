val=['1000','900','500','400','100','90','50','40','10','9','5','4','1']
symbol=["M","CM","D","CD","D","XD","L","XL","X","IX","V","IV","I"]
num=int(input("enter a integer number:"))
roman=""
k=0
list=[]
while k<len(val):
    values=int(val[k])
    list.append(values)
    k=k+1
# print(list)
    for i in range(len(list)):
        m=num//list[i]
        num=num%list[i]
        for j in range(m):
            roman+=symbol[i]
        num=num%list[i]
print(roman)