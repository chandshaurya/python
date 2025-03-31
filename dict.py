info= {'name':'Shaurya', 'age':18, 'degree':'Btech'}
print(info)
print(type(info))

print(info.items())
print(info.keys())
print(info.values())

for keys in info.keys():
    print(keys)

for keys,values in info.items():
    print(f" The value corresponding to key {keys} is values {values}")


### methods

info.update({'DOB':2006})
print(info)

info.pop('DOB')
print(info)

info.popitem()
print(info)

# info.clear()
# del info

