#To print n fibonacci number
f1=0
f2=1
n=int(input("Enter the number: "))
if n<0:
    print("Invalid input")
elif n==0:
    print(f1)
else:    
    for i in range(1,n+1):
        print(f1)
        f=f1+f2
        f1=f2
        f2=f


