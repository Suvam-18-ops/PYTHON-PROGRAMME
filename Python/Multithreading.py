import threading

def my_task():
    for i in range(5):
        print(" Child Thread is running")

t1 = threading.Thread(target=my_task)
t1.start()
for i in range(5):
        print(" Main Thread is running")