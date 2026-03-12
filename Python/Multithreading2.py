import threading

class MyThread(threading.Thread):
    def run(self):

       for i in range(5):
           print(" Child Thread is running")
t1 = MyThread()
t1.start()
for i in range(5):
        print(" Main Thread is running")