l= [29,12,1,5,13, "Shaurya"]
print(l)

print(l[:])
print(l[0:5:2])
print(l[-1])
print(l[-2])

if 29 in l :
    print("yes")
else:
    print("no")

if "Sh" in "Shaurya" :
    print("yes")

lst = [i*i for i in range(11)]
print(lst)

lst1= [i*i for i in range(11) if i%2==0]
print(lst1)


print(l)
l.append(89)
print(l)

l.append(1)
l.append(29)
print(l)

print(l.index(1))
print(l.index(29))

#m = l 
#m[0]=0
#print(l)

l.reverse()
print(l)

m= l.copy()
m[0]= 0
print(l)

l.insert(1,89)
print(l)

k = l+lst
print(k)






