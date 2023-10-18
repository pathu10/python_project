#greatest among three integers using comditional operator

print("Enter the three number")
a=int(input(" "))
b=int(input(" "))
c=int(input(" "))
if a>b:
    if a>c:
        print("Greatest among",a,b,c,"is",a)
    else:
        print("Greatest among",a,b,c,"is",c)
elif b>c:
    print("Greatest among",a,b,c,"is",b)
else:
    print("Greatest among",a,b,c,"is",c)



