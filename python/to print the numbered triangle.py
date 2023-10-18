#To print triangle (right angle)
n=int(input("Enter the number: "))
if n<=0:
    print("Invalid input")
else:    
    for i in range(n+1):
        for j in range(i):
            print(i,end=" ")
        print("\n")


