#This is a Calculator
#I made this Calculator with python
#Thank you - "code with Harry " "Apna college" "python organization"
#-------------------------------------------------------------------
num1=float(input("enter a number:  "))
op=input("enter a operator: +,-,*,/,%:  ")
num2=float(input("enter a number:  "))
if op=="+":
    print(num1,op,num2,"=",num1+num2)
elif op=="-":
    print(num1,op,num2,"=",num1-num2)
elif op=="*":
    print(num1,"X",num2,"=",num1*num2)
elif op=="/": 
    print(num1,op,num2,"=",num1/num2)
elif op=="%":
    print(num1,op,num2,"=",num1%num2)
else :
    print("Invalid operation")
