def fib(num):
    if (num==0 or num==1):
        return num
    else:
        return(fib(num-1)+fib(num-2))

num = int(input("Enter a no :"))
print(fib(num))