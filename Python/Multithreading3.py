# import time

# def task(name):
#     print(f"Starting {name}")
#     time.sleep(2)
#     print(f"Finished {name}")

# start = time.time()

# task("Task 1")
# task("Task 2")
# task("Task 3")

# end = time.time()

# print("Total Time:", end - start)
import threading
import time

def task(name):
    print(f"Starting {name}")
    time.sleep(2)
    print(f"Finished {name}")

start = time.time()

t1 = threading.Thread(target=task, args=("Task 1",))
t2 = threading.Thread(target=task, args=("Task 2",))
t3 = threading.Thread(target=task, args=("Task 3",))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

end = time.time()

print("Total Time:", end - start)