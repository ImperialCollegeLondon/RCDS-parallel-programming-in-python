import multiprocessing
import ctypes

def increment(v):
    v.value += 1

# Create a shared memory value
# It is an integer with an initial value of 0
v = multiprocessing.Value(ctypes.c_int, 0)

# Create a process that increments the value
p = multiprocessing.Process(target=increment, args=(v,))
p.start()
p.join()

# Print the value
print(v.value)

