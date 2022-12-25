#2
alphabet="ABCDEFGHIJK"

for i in range(0,6,1):
    letters = alphabet[(11-2*i):]
    strip = alphabet.rstrip(letters)
    row = strip.center(11)
    print(row)


