import multiprocessing
import ctypes

def increment(v):
    # Manually acquire and release the lock
    v.get_lock().acquire()
    v.value += 1
    v.get_lock().release()

    # Use the context manager to acquire and release the lock
    with v.get_lock():
        v.value += 100

# Create a shared memory value
# It is an integer with an initial value of 0
v = multiprocessing.Value(ctypes.c_int, 0)

# Create n_process processes which increment the value
n_process = 8
processes = []
for i in range(n_process):
    p = multiprocessing.Process(target=increment, args=(v,))
    p.start()
    processes.append(p)

for i in range(n_process):
    p.join()

# Print the value
print(v.value)