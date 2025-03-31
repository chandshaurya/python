s={2,3,4,6,7,23,45,1}
print(s)   ##unordered

print(type(s))
sky= {}
print(type(sky))  ### ambiguity in compiler

set = set({})
print(type(set))

for value in  s:
    print(value)


## JOINING SETS

s1= {1,2,4,7,11}
s2 = {3,4,1,44,23}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.symmetric_difference(s2))


s1.update(s2)
print(s1)

## set methods

s3= {8,9,10,15}

print(s1.isdisjoint(s3))
print(s1.issubset(s2))
print(s1.issuperset(s3))

s1.remove(11)
print(s1)

s1.add(123)
print(s1)

items = s3.pop()
print(s3)
print(items)

#del s3

s3.clear() 
print(s3)





    
  


