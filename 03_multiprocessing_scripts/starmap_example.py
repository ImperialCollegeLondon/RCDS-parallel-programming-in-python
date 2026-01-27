from multiprocessing import Pool, current_process
import time
import random

# This is the function we want to apply to pairs of values in a list
def g(x, y):
    print(f'Process {current_process().name} is working on the values {x} and {y}')
    # Wait a random time between 0 and 1 seconds
    time.sleep(random.uniform(0, 1))
    # Perform a simple calculation and return the result
    return x * y

# Create a list of values to apply the function to
data = [(i, i+1) for i in range(10)]
print(data)

# Create a Pool object with 4 processes
# The Pool will be discarded when the block is exited
with Pool(4) as p:
    # Apply the function g to each set of arguments in a list
    output = p.starmap(g, data)

# Print the output
print(output)