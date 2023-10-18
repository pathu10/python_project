#to check prime or not
n=int(input("Enter the number: "))
c=0
if n<=0:
    print('Invalid input')
for i in range(1,n+1):
    if n%i==0:
        c=c+1

if c==2 :
    print(n,"is Prime")
else:
    print(n,"is not Prime")
