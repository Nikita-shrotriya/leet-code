n=int(input("enter the num"))
i=2
sum=1
while i<=n//2:
    if n%i==0:
        sum=sum+i
    i=i+1
if sum==n:
    print(n,"is a perfact number")
else:
    print(n,"is a not perfact number")