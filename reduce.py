
from functools import reduce

numbers= [1,5,8,7,9,6,5]

sum= reduce(lambda x,y:x+y, numbers)
print(sum)