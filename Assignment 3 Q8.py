#8
Set1 = [1,2,3,4,5]
Set2 = [2,4,6,8]
Set3 = [1,5,9,13,17]
Set4 = Set1+Set2+Set3
#a
Set5 = []
for i in range(14):
    x = Set4[i]
    if x in Set1 and x not in Set2 or x in Set2 and x not in Set1:
        Set5.append(x)
    else:
        continue
print(Set5)

#b
Set6 = []
for j in range(14):
    y = Set4[j]
    if y in Set1 and y not in Set2 and y not in Set3  or y in Set2 and y not in Set3 and y not in Set1 or y in Set3 and y not in Set2 and y not in Set1:
        Set6.append(y)
    else:
        continue
print(Set6)

#c
Set7 = []
for k in range(14):
    z = Set4[k]
    if z in Set1 and z in Set2 and z not in Set3 or z in Set2 and z in Set3 and z not in Set1 or z in Set2 and z in Set3 and z not in Set1:
        Set7.append(z)
    else:
        continue
print(Set7)

#d
Set8 = []
for m in range(14):
    l = Set4[m]
    if l in Set2 or l in Set3 and 1<=l<=10:
        if l not in Set1:
             Set8.append(l)
        else:
            continue
    else:
         continue
print(Set8)

#e
Set10 = []
for o in range(1,11):
   if o not in Set4:
       Set10.append(o)
   else:
       continue
print(Set10)










