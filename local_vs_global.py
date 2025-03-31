
x= 10  # global
y=1
def sky():
    y=5   # local 
    print(y)

sky()
print(x)
print(y)


# we can change global var 

x= 10  # global

def sky():
    global x 
    x=4
    y=5   # local 
    print(y)

sky()
print(x)

