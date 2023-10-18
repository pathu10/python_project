#reversing a number and checking whether it is palindrome or not
rev=0
n=int(input("Enter the number: "))
temp=n
while n!=0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("Reverse of the number is",rev)
if temp==rev:
    print(temp,"is Palindome")
else:
    print(temp,"is not Panlindrome")
