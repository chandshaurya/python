import time

t= time.strftime('%H:%M:%S')
print(t)

hours= int(time.strftime('%H'))

if(hours>= 0 and hours<12):
    print("Good morning")
elif(hours> 12 and hours<5):
    print("Good afternoon ")
else:
    print("Good Night")


