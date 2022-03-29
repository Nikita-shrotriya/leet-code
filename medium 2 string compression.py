chars = ["a","a","b","b","c","c","c"]
i=0
a=[]
while i<len(chars):
    count=0
    b=[]
    j=0
    while j<len(chars):
        if chars[i]==chars[j]:
            count=count+1
        j=j+1
    b.append(chars[i])
    b.append(count)
    if b not in a:
        a.append(b)
    i=i+1
print(a)
