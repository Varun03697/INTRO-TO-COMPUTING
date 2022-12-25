#6
StudentData = {}
for i in range(3):
    Value = input("Name of student:")
    Key = input("SID of Student:")
    StudentData[Key] = Value

#a
print(StudentData.items())

#b
SortedByKey = sorted(StudentData.items())
print(SortedByKey)

#c
SortedByValue = {k:v for k, v in sorted(StudentData.items(),key=lambda v: v[1])}
print(SortedByValue)



