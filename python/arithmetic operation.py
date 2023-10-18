#To perform arithmetic operation

a,op,b=int(input("Enter the number: ")),str(input("Enter the operator: ")),int(input("Enter the number: "))
if op=='+':
    print(a,"+",b,"=",a+b)

elif op=='-':
        print(a,"-",b,"=",a-b)
        
elif op=='*':
        print(a,"*",b,"=",a*b)

elif op=='%':
        print(a,"%",b,"=",a%b)

elif op=='/':
    if b==0:
        print("divide by zero error")
    print(a,"/",b,"=",a/b)

else:
    print("Inavlid Expression")
