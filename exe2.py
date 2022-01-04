print("enter the first number")
num1=int(input())
print("enter the second number")
num2=int(input())
print("enter the operator")
operator=input()
if operator=='+':
    if num1==56 and num2==9:
        print("Result:7777")
    else: 
        print('Result:',num1+num2)
elif operator=='-':
    if num1==45 and num2==54:
        print("Result: 5234")
    else:
        print("Result:",num1-num2)
elif operator=='*':
    if num1==45 and num2==3:
        print("Result:3423")
    else:
        print("Result:",num1*num2) 
elif operator=='/':
    if num1==56 and num2==6:
        print("Result:123")
    else:
        print("Result: ",num1/num2) 