#QUESTION NO. 1
Marks = int(input("Enter the grades:"))
if Marks < 25:
    print("Your grade is F")
elif 25 <= Marks < 45:
    print("Your grade is E")
elif 45 <= Marks < 50:
    print("Your grade is D")
elif 50 <= Marks < 60:
    print("Your grade is C")
elif 60 <= Marks < 80:
    print("Your grade is B")
elif Marks >= 80:
    print("Your grade is A")
else:
    print("Invalid Input")

#QUESTION NO. 2
Year = int(input("Enter the year:"))
if Year % 4 != 0 or (Year % 100 == 0 and Year % 400 != 0 ):
    print(f"{Year} is not a leap year")
else:
    print(f"{Year} is a leap year")

#QUESTION N0. 3
import random
list = [i for i in range(1,10)]
marks = 0
for i in range(10):
    x = random.choice(list)
    y = random.choice(list)
    print()
    z = int(input(f"Question no. {i+1}: {x}*{y}:"))
    if z == x*y:
        print("Your answer is correct")
        marks = marks + 1
    else:
        print("Your answer is wrong")
print("Your marks are:\n",marks)

#QUESTION N0. 4
for CANDY in range(1,201):

    if CANDY % 5 == 2 and CANDY % 6 == 3 and CANDY % 7 == 2:
        print(F" No of pieces are {CANDY}")
        break
    else:
        continue