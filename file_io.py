
f=open('my.txt','r')
content= f.read()
print(content)
f.close()

f= open('my.txt','a')
f.write('shaurya kaushik  ')
f.close()


f=open('my.txt','r')
while True:
    line= f.readlines()
    if not line:
        break
    print(line)
f.close()

f= open('my1.txt','r')
i=0
while True:
    i=i+1
    line=f.readlines()
    if not line:
        break
    m1= line.strip().split(',')[0]
    m2= line.strip().split(',')[1]
    m3= line.strip().split(',')[2]

    print(f" mark of student {i} in maths is : {m1}")
    print(f" mark of student {i} in maths is : {m2}")
    print(f" mark of student {i} in maths is : {m3}")





