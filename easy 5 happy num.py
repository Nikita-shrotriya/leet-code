from unicodedata import digit


n=int(input("enter the num"))
sum=0
num=n
while sum!=1 and sum!=4:
    sum=0
    while n>0:
        digit=n%10
        sum=sum+digit*digit
        n=n//10
    n=sum
if sum==1:
    print(num,"is a happy number")
else:
    print(num,"is not a happy number")
