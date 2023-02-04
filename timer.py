import threading
import time

def task():
    print("The task is executed")

thread = threading.Timer(5, task)
thread.start()
print("sleeping for 3 seconds")
time.sleep(3)
print("cancelling the timer thread")
thread.cancel()
