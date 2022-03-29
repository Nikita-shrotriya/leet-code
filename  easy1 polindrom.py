x=int(input("enter"))
rev=0
n=x
while x>0:
    rev=rev*10+x%10

    x=x//10
if n==rev:
    print(n,"palindrom")
else:
    print(n,"not palindrom")