#4
t=float(input("Enter the grades:"))
if (t==10):
    print("Your grade is 'A+' and Outstanding Performance")
elif(9<=t<10):
    print("Your grade is 'A' and Excellent Performance")
elif(8<=t<9):
    print("Your grade is 'B+' and Very Good")
elif(7<=t<8):
    print("Your grade is 'B' and Good")
elif(6<=t<7):
    print("Your grade is 'C+' and Average")
elif(5<=t<6):
    print("Your grade is 'C' and Below Average")
elif(4<=t<5):
    print("Your grade is 'D' and Poor")
else:
    print("Out of Range")
