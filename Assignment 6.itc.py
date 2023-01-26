#QUESTION NO. 1
num = int(input("Enter the number:"))
def perfect_number_checker(k):
    list = []
    for i in range(1,k):
        if k % i == 0:
            list.append(i)
        else:
            continue
    m = 0
    for j in list:
        m = m + j
    if m == k:
        return("Yes, it is a perfect number")
    else:
        return("No, it is not a perfect number")
print(perfect_number_checker(num))

#QUESTION NO. 2
string = str(input("Enter the string:"))
new_string = string.replace(' ','')
def reverse(z):
    if z == "":
        return(z)
    else:
        return reverse(z[1:]) + z[0]
reverse_string = str(reverse(new_string))
for i in range(len(new_string)-1):
    if new_string[i] == reverse_string[i] and 0 <= i < len(new_string)-2:
        continue
    elif new_string[i] != reverse_string[i]:
        print("Not an palindrome")
        break
    elif new_string[i] == reverse_string[i]:
        print("It is a palindrome")
    else:
        print("Invalid Input")

#QUESTION NO. 3
rows = int(input("Enter the no. of rows:"))
def factorial(n):
    if n==0:
        return(1)
    else:
        return n * (factorial(n-1))
def C(r,n):
    if  n >= 0 and r >= 0 and n >= r:
        return int(factorial(n)/(factorial(r) * factorial(n-r)))
    else:
        return"invalid input"
for n in range(rows+1):
    for r in range(0,n+1):
        print(C(r,n),end=' ')
        t = str(C(r,n))
        t.center(rows+1)
    print(" ")

#QUESTION NO. 4
string = str(input("Enter the string:"))
new__string = string.replace(' ','')
new_string = new__string.upper()
set1 = set(new_string)
list1 = list(set1)
list1.sort()
import string
list2 = list(string.ascii_uppercase)
if list1 == list2:
    print('Yes')
else:
    print("No")

#QUESTION NO. 6
def student_data(student_id, student_name=None, student_class=None):
    print("Student ID:", student_id)
    if student_name:
        print("Student Name:", student_name)
    if student_class:
        print("Student Class:", student_class)
student_data(12534, student_name="Varun", student_class="5th")


#QUESTION NO. 8
a = [-25,-10,-7,-3,2,4,8,10]
x = []
for i in a:
    for j in a:
        for k in a:
            if i+j+k == 0:
                x.append([i,j,k])
            else:
                continue
y = []
for m in x:
    m.sort()
    y.append(m)
list2 = []
for m in y:
    if m not in list2:
        list2.append(m)
print(list2)

















































