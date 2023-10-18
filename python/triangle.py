#To print triangle (right angle)
n=int(input("Enter the number of rows: "))
if n<=0:
    print("Invalid input")
else:    
    for i in range(n):
        for j in range(n-i):
            print('*',end=" ")
        print("\n")

