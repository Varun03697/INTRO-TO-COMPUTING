#1
string="Python is a case sensitive language"

#a
print(len(string))

#b
reverse=string[::-1]
print(reverse)

#c
slice = slice(10,26)
print(string[slice])

#d
print(string.replace("a case sensitive","object oriented"))

#e
NewString=string.index('a')
print(NewString)

#f
print(string.replace(' ',''))