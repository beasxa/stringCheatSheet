str = "beasley"

# the 'in' syntax - will show if letter or substring exists
print('x' in str)  # will return false
print('a' in str)  # will return true

# slicing
str[1]  # e
str[-1]  # y
str[4:6]  # le
str[:4]  #beas
str[-3:]  #ley

# iterating through string
for x in str:
   print(x)

# length of string
length = len(str)
print(length)

# prints length of array
arr = ['red', 'pink', 'white']
lengthArr = len(arr)
print(lengthArr)

# .lower() method
newstr = str.lower()
print(newstr)

# .upper() method
newstr2 = str.upper()
print(newstr2)

# .strip() method
fancystr = "     ......Lemons and limes......     "
newfancy = fancystr.strip()
print(newfancy)

fancystr2 = "....+...lemons and limes ...-..."
print(fancystr2.strip('.')) # +...lemons and limes ...-
print(fancystr2.strip('.+-')) #lemons and limes

# .title() method - returns first letter captial
titlestr = 'guardians of the galaxy'
print(titlestr.title()) # returns Guardians Of The Galaxy

# .split() method
print(titlestr.split()) # returns ['guardians', 'of', 'the', 'galaxy']
print(titlestr.split('a')) # returns ['gu', 'rdi', 'ns of the g', 'l', 'xy']

# .find() method
print(titlestr.find('a')) # returns 2 - index of first instance

# .replace() method
print(titlestr.replace('a', 'A')) # returns 'guArdiAns of the gAlAxy'

# .join() method
myarr = ['i', 'am', 'the', 'best']
joinedarr = '-'.join(myarr)
print(joinedarr)

mylist = '-'.join(['ashley', 'is', 'awesome'])
print(mylist) # returns ashley-is-awesome

