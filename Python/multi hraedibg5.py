import threading

def task():
    print("Current Thread Name:", threading.current_thread().name)
threading.current_thread().name="Suvam"
print("Current Thread Name:", threading.current_thread().name)
t1 = threading.Thread(target=task)
t1.name="Radhe"
t1.start()
t1.join()
