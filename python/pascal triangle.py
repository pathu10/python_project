#To print pascal triangle 
n=int(input("Enter the number of rows: "))
if n<=0:
    print("Invalid input")

for r in range(1,n+1):
    for s in range(n-r+1):
            print(end=" ")
    b=1
    for c in range(1,r+1):
        print(b,sep=" ",end=" ")
        b=b*(r-c)//c
    print("\n")


