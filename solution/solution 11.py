#armstrong number
n=int(input("enter any number:"))
sum=0
temp=n
while(temp>0):
    digit=temp%10
    sum+=digit**3
    temp//=10
if(n==sum):
    print(n,"is armstrong number")
else:
    print(n,"is not armstrong number")
