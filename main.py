import threading
import time

def counter(n):
    for i in range(n):
        print(f"{i}")
        time.sleep(1)

thread = threading.Thread(
    target=counter, name='counter', args=(5,), daemon=True)
thread.start()
# thread.join()
print("End of program")