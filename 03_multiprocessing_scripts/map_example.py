from multiprocessing import Pool, current_process
import time
import random

# This is the function we want to apply to each entry in a list
def f(x):
    # multiprocessing.current_process().name is a way to get the name of the process
    print(f'Process {current_process().name} is working on the value {x}')
    # Wait for a random amount of time between 0 and 1 seconds
    time.sleep(random.uniform(0, 1))
    # Perform a simple calculation and return the result
    return x * x

# Create a list of values to apply the function to
data = list(range(10))
print(data)

# Create a Pool object with 4 processes
# The Pool will be discarded when the block is exited
with Pool(4) as p:
    # Apply the function f to each entry in the list
    output = p.map(f, data)

# Print the output
print(output)