
# compare three value 

a= int(input("enter : "))
b= int(input("enter : "))
c= int(input("enter : "))

print("the largest among three no is : ")
print(a) if((a>b) and (a>c)) else print(b) if(b>c) else print(c)