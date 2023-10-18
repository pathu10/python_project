#factorial of number

#def fact(n):
fact=1
i=1  # can be assigned or in for loop range enter start as 1
n=int(input("Enter the number: "))
if n<0:
    print("Invalid input")
elif n==0:
    print("Factroial of ",n,"is",1)
else:
    for i in range(i,n+1):
        fact=fact*i
    print("Factorial of",n,"is",fact)
