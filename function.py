def avg(a=9,b=1):
    print((a+b)/2)


avg(5,6)
avg()
avg(1)   
avg(b=9)

print(type(avg))

# arbitary arguments 

def average(*numbers):
    sum=0
    for i in numbers:
        sum= sum +i
    print(sum/len(numbers))


average(3,89,55)


# keyword arbitary arguments
def name(** name):
    print("hello ", name["fname"],name["lname"])

name(fname="shaurya", lname="kaushik")
    