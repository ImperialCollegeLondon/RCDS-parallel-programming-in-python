import numpy as np
import multiprocessing
import time

# Note the start time
start_time = time.time()

def find_smallest_multiple(n_data, factor, queue):
    # This function generates n_data random integers and finds the smallest multiple of factor

    # Initially we have found no multiples of factor
    result = None

    # Create the random data
    data = np.random.randint(1, 1000, n_data)

    for d in data:
        # Loop over the data and check if it's a multiple of factor
        if d % factor == 0:
            # If it is, check if it's the smallest we've found so far
            if result is None or d < result:
                # Update the result
                result = d

    # After considering each value, put the result in the queue
    queue.put(result)

# Set up the problem data
n_processes = 2
n_data = int(1e6)
factor = 7
n_data_per_process = n_data // n_processes

# Set up the queue
queue = multiprocessing.Queue()

for i in range(n_processes):
    # Spawn and start the processes
    p = multiprocessing.Process(target=find_smallest_multiple, args=(n_data_per_process, factor, queue))
    p.start()

# We haven't found any multiples of factor yet
result = None

for i in range(n_processes):
    # Get each result from the queue
    # The code will pause here while the main process waits for each child process to finish
    r = queue.get()

    if result is None or r < result:
        # If it's smaller than the current result, update it
        result = r

# Note the end time and print the elapsed time
end_time = time.time()
print(f'Time taken: {end_time - start_time}')

print(f'The smallest multiple of {factor} in the data is {result}')

