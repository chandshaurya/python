
import threading
l= [1,8,5,2,6]
print(l)

newl=[]
for item in l:
    newl.append(lambda x: x**2)

newl= list(map(lambda x: x**2,l))

print(newl)



def increment(counter, lock):
    for i in range(10000):
        lock.acquire()
        counter += 1
        lock.release()

if __name__ == '__main__':
    counter = 0
    lock = threading.Lock()

    threads = []
    for i in range(2):
        thread = threading.Thread(target=increment, args=(counter, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Counter value:", counter)
