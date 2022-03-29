a=5
b=10
while(b!=0):
    carry=a&b
    a=a^b
    b=carry<<1
print(a)