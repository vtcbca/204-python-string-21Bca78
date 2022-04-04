#maximum number
num1=float(input("enter first number1:"))
num2=float(input("enter first number2:"))
num3=float(input("enter first number3:"))
if(num1>num2)and(num1>num3):
    maximum=num1
elif(num2>num1)and(num2>num3):
    maximum=num2
else:
    maximum=num3
print("the maximum namber is",maximum)
    
