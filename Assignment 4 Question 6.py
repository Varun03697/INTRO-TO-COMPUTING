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





#

















