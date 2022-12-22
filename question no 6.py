#6
a=int(input("First Side:"))
b=int(input("Second Side:"))
c=int(input("Third Side:"))
if (a+b > c and b+c > a and c+a > b):
    print("Yes")
else:
    print("No")