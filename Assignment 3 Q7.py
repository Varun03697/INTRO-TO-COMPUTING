#7
NoOfTerms = int(input("Enter the number:"))
Num1=0
Num2=1
Num3=0
for i in range(NoOfTerms):
    Num4=Num1+Num2
    Num1=Num2
    Num2=Num4
    print(Num4,sep=',')
    Num3=Num3+Num4

AverageOfNumbers = Num3/NoOfTerms

AverageOfNumbers = print("The Average is:",AverageOfNumbers)



