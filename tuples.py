tup = [29, 89, 1, 89, 'Shaurya', 13, 5, 1, 12, 29, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(tup)

t= (4)
print(type(t))
t=(4,)
print(type(t))

if 13 in tup:
    print("yes")

print(tup.count(1))
print(tup.index(29,1,10))

#Manupulating_Tuble

tup = [29, 89, 1, 89, 'Shaurya', 13, 5, 1, 12, 29, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
temp = list(tup)
temp.append("sky")
temp.pop(0)
temp[1]= "Tannu"
tup = tuple(temp)
print(tup)
