# code 1

a= input("enter : ")
print(f"Multiplication table of {a} is ")
try:
    for i in range(1,11):
        print(f"{int(a)}* {i} = {int(a)*i}")
    
except ValueError:
    print("invalid input")

print("code working fine ")

# code 2
try:
   num = int(input("enter : "))
   l= [1,2,3]
   print(a[num])

    
except ValueError:
    print("not an int ")

except IndexError:
    print("Index error ")


# code 3

a= int(input("enter : "))

try:
    res= 100/a
except ZeroDivisionError:
    print("Error")

else:
    print("result is :", res)


# code 4

a= int(input("enter : "))

try:
    res= 100/a
except ZeroDivisionError:
    print("Error")

finally:
    print("result is :", res)









