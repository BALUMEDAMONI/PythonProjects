from array import *

# If you know the range
vals = array('i', [2, 4, 6, 8])

for i in range(4):  # directly using known range
    print(vals[i])


# Without knowing the range
vals = array('i', [2, 4, 6, 8])
for i in range(len(vals)):
    print(vals[i])


# Direct method (for-each loop)
vals = array('i', [2, 4, 6, 8])
for e in vals:
    print(e)


# Creating new array with squared values
vals = array('i', [2, 4, 6, 8])

newArr = array(vals.typecode, (a * a for a in vals))  # square each element
for e in newArr:
    print(e)
