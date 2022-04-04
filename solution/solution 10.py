#pallindrome number or not
n=int(input("enter number:"))
temp=n
rev=0
while(n>0):
    a=n%10
    rev=rev*10+a
    n=n//10
if(temp==rev):
    print("the number is pallindrome")
else:
    print("the number is not pallindrome")
