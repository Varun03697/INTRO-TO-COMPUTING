#QUESTION NO.1

string = str(input("Enter the string:"))
def reverse(s):
    if len(s) == 1:
        return s
    else:
        return reverse(s[1:]) + s[0]
print(reverse(string))

#QUESTION NO. 2

x = int(input("Enter the number:"))
y = int(input("Enter the range:"))

for i in range(1,(y // x)+1):
    print(4*i , end=",")
print("")

#QUESTION NO. 3:

a = float(input("Enter the length of first side:"))
b = float(input("Enter the length of second side:"))
c = float(input("Enter the length of third side:"))

if a+b > c and b+c > a and c+a > b and a>0 and b>0 and c>0:
    print("Triangle is possible ")
    def area(x, y, z):
        import math
        s = (x + y + z) / 2
        return math.sqrt(s * (s - x) * (s - y) * (s - z))
    print(area(a, b, c))
else:
    print("Triangle is not possible")



#QUESTION NO 4

x = "*"
for i in range(5):
    print(x*i)
for k in range(5,0,-1):
    print(x*k)

#QUESTION NO 5
n = int(input("Enter the number of rows:"))
import string
x = [i for i in string.ascii_uppercase]
def letters(m):
    y = m % 26
    return(x[y])

k=0
for i in range(0,n):
    for j in range(k,k+i+1):
        print(letters(j) , end='')
        k = k+1
    print('')

#QUESTION NO. 6

x = int(input("Enter the number:"))
def primenumber(n):
    if n == 1:
        return("No")
    elif n == 2:
        return("Yes")
    else:
        for i in range(2,n):
            if n % i == 0:
                return ("No")
                break
            elif n % i != 0 and i < n-1:
                continue
            else:
                return ("Yes")

for k in range(1,x+1):
    if primenumber(k) == "No":
        continue
    else:
        print(k , end=',')
print("")

#QUESTION NO. 7

for i in range(1,501):
    if i%7==0 and i%11==0:
        print(i)
    else:
        continue

#QUESTION NO 8

Positive_Numbers = []
Negative_Numbers = []
Odd_Numbers = []
Even_Numbers = []
list = []
for i in range(10):
    x = int(input("Enter the number:"))
    list.append(x)
print("List is:",list)
for j in list:
    if j > 0:
        Positive_Numbers.append(j)
    else:
        continue
for k in list:
    if k < 0:
        Negative_Numbers.append(k)
    else:
        continue
for l in list:
    if l % 2 != 0:
        Odd_Numbers.append(l)
    else:
        continue
for m in list:
    if m % 2 == 0:
        Even_Numbers.append(m)
    else:
        continue
print('Positive_Numbers:\n',Positive_Numbers )
print('Negative_Numbers:\n',Negative_Numbers)
print('Odd_Numbers:\n',Odd_Numbers)
print('Even_Numbers:\n',Even_Numbers)
dict1 = {}
for i in list:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] = dict1[i]+1
for i in dict1.keys():
    print(f"{i} occurs {dict1[i]} times in the list")

#QUESTION NO. 9

list1 = []
for i in range(5):
    x = str(input("Enter the element:"))
    list1.append(x)
dict1 = {}
for i in list1:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] = dict1[i]+1
for i in dict1.keys():
    print(f"{i} occurs {dict1[i]} times in the list")