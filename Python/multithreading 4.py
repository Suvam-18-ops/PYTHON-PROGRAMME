import threading
import time

class MyThread(threading.Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f"Starting {self.name}")
        time.sleep(2)
        print(f"Finished {self.name}")

start = time.time()

t1 = MyThread("Task 1")
t2 = MyThread("Task 2")
t3 = MyThread("Task 3")

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

end = time.time()

print("Total Time:", end - start)