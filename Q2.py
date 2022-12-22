#2
GrossIncome=int(input("Gross Income:"))
NoOfDependents=int(input("No. of dependents:"))

TaxableIncome=(GrossIncome-10000-(NoOfDependents * 3000))
print("Tax:",TaxableIncome*(20/100))







